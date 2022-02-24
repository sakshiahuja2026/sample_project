from dataclasses import field
from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import task
from django.views.generic import DetailView
# Create your views here.
class createtask(CreateView):
    model = task
    fields= ['task_name' , 'task_description']
    template_name='task/create.html'
    success_url='/task/view/'

class Deletetask(DeleteView):
    model=task
    success_url='/task/view/'

def index(request):
    return render(request, 'task/index.html')

class Updatetask(UpdateView):
    model = task
    fields= ['task_name' , 'task_description']
    template_name='task/update_task.html'
    success_url='/task/view/'

class taskDetail(DetailView):
     model=task
     template_name='task/detail_task.html'
    