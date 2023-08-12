from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from app.models import *
# Create your views here.
class Triner_List(ListView):
    model=Triner
    template_name='Triner_List.html'
    context_object_name='tl'
    #queryset=Triner.objects.filter(triner_name='rakesh')
    ordering=['triner_name']


