from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import Taskform

def task_list(request):
    tasks=Task.objects.all()
    return render(request,'index.html',{'tasks':tasks})
def create_task(request):
    if request.method=='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=Taskform()
    return render(request,'task_form.html',{'form':form})
def update_task(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=='POST':
        form=Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=Taskform(instance=task)
    return render(request,'task_form.html',{'form':form})
def delete_task(request,id):
    task=get_object_or_404(Task,id=id)
    task.delete()
    return redirect('task_list')