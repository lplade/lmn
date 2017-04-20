from django.shortcuts import render
from django.views.generic.edit import DeleteView # this is the generic view
from django.urls import reverse_lazy
from lmn.models import Note


def homepage(request):
    return render(request, 'lmn/home.html')
