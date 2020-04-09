""" This is the urls for sign up and sign pages for regular users """
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]
