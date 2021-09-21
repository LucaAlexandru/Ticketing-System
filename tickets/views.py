from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from tickets.models import Ticket
from django.http import HttpResponseRedirect
from tickets.forms import TicketForm, EditTicketForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def secret_view(request):
    return TemplateResponse(request, "index.html")


def view_database(request):
    data = Ticket.objects.all()
    return TemplateResponse(request, "ticket_data.html", {"data1": data})


def view_databasetwo(request):
    data = Ticket.objects.filter(assignee='Bob')
    return TemplateResponse(request, "ticket_data.html", {"data1": data})


def view_ticket_details(request, ticket_id):
    print(ticket_id)
    return TemplateResponse(request, "index.html")


@login_required(login_url="/accounts/login/")
def add_to_database(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("new_code"))
            cleaned_code = form.cleaned_data.get("new_code")
            cleaned_bug = form.cleaned_data.get("new_bug")
            cleaned_created = form.cleaned_data.get("new_created")
            cleaned_assignee = form.cleaned_data.get("new_assignee")
            cleaned_due = form.cleaned_data.get("new_due")
            cleaned_status = form.cleaned_data.get("new_status")
            cleaned_severity = form.cleaned_data.get("new_severity")
            new_ticket = Ticket(code=cleaned_code, bug=cleaned_bug,
                                created=cleaned_created, assignee=cleaned_assignee,
                                due=cleaned_due, status=cleaned_status,
                                severity=cleaned_severity)
            new_ticket.save()
            # return HttpResponseRedirect('thanks')
            return redirect("database_view")
        else:
            return HttpResponseRedirect('not valid')
    else:
        form = TicketForm()
    return render(request, 'add_to_database.html', {'ticket_form': form})


def edit_ticket(request, ticket_id):
    print(request.user)
    ticket = Ticket.objects.get(id=ticket_id)
    if ticket.user != request.user:
        return redirect("database_view")
    if request.method == 'POST':
        form = EditTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("database_view")
        else:
            return HttpResponseRedirect('not valid')
    else:
        form = EditTicketForm(instance=ticket)
    return render(request, 'edit_ticket.html', {'edit_form':form})


def edit_in_database(request):
    ticket = Ticket.objects.get(id=1)
    ticket = Ticket.objects.all().first()
    ticket.assignee = "Tudor"
    ticket.save()
    return TemplateResponse(request, "index.html", {})


def find_in_database(request):
    all_tickets = Ticket.objects.all()
    found_ticket = None
    for a_ticket in all_tickets:
        if a_ticket.assignee == "Victor":
            found_ticket = a_ticket
            break
    print(found_ticket.assignee)
    return TemplateResponse(request, "index.html", {})


def delete(request, ticket_id):
    emp = Ticket.objects.get(pk=ticket_id)
    if emp.severity != "Major":
        emp.delete()
    else:
        messages.error(request, 'Can\'t delete tickets with Major severity.')
    return redirect("database_view")


def change_status(request, ticket_id):
    emp = Ticket.objects.get(pk=ticket_id)
    if emp.status == "Closed":
        emp.status = "Open"
        emp.save()
    elif emp.status == "Open":
        emp.status = "Closed"
        emp.save()
    else:
        messages.error(request, 'Can\'t change status other than for open/closed tickets.')
    return redirect("database_view")


def change_all_entries(request):
    all_tickets = Ticket.objects.all()
    name_seed = "a"
    for a_ticket in all_tickets:
        a_ticket.code = name_seed
        a_ticket.save()
        name_seed += "b"
    return TemplateResponse(request, "index.html", {})
