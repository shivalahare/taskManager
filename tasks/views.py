from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm ,SignUpForm

@login_required
def taskList(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('taskList')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def updateTask(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('taskList')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def deleteTask(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('taskList')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('taskList')  # Redirect to the task list after signup
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})