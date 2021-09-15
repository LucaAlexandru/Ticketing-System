"""ticketing_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.homepage, name="homepage"),
    path('about/', views.about),
    path('add_to_database/', views.add_to_database),
    path('edit_in_database/', views.edit_in_database),
    path('find_in_database/', views.find_in_database),
    path('change_all_entries/', views.change_all_entries),
    path('view_database/', views.view_database, name="database_view"),
    path('view_databasetwo/', views.view_databasetwo),
    path('<int:ticket_id>/', views.view_ticket_details),
    path('delete/<int:ticket_id>/', views.delete),
    path('change_status/<int:ticket_id>/', views.change_status)
]
