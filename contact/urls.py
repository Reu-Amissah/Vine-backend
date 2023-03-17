from django.urls import path

from . import views

# from .views import api_contact

urlpatterns = [
    path('', views.endpoints),
    path('contacts/', views.contact_message),
    path('contact-post/', views.contact_post),
]