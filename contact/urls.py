from django.urls import path

from . import views

# from .views import api_contact

urlpatterns = [
    path('', views.contact_message)
]