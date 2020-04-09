"""This will be the main page that shows all the attributes in the root"""

from django.shortcuts import render
from .models import Work

# The main view comes here.


def index(request):
    all_work = Work.objects.all
    return render(request, "index.html", {'all': all_work})
