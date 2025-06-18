from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.

def addTask(request):
    task=(request.POST['task'])
    Task.objects.create(task=task)
    return redirect('home')

def updateTask(request, pk):
    task= get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task = request.POST['task']
        get_task.task = task
        get_task.save()
        return redirect('home')
    else:
        context= {
            'get_task': get_task,
        }
    return render(request, 'edit.html', context)

def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')


 

