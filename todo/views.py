from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task
from django.shortcuts import redirect

# Create your views here.

def addTask(request):
    task=(request.POST['task'])
    Task.objects.create(task=task)
    return redirect('home')