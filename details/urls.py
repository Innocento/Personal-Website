"""This is the urls for the details app that show a page in my online footprint"""

from django.urls import path
from . import views

# Url mappings of the details app in details folder
urlpatterns = [
    path('', views.index, name='index'),
]
