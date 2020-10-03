from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
# Create your views here.
from .forms import TaskForm

def index(request):
	tasks = Task.objects.all().order_by('-created')
	form = TaskForm()
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('task:index')
	context = {
		'form': form,
		'tasks': tasks
	}
	return render(request, 'task/list.html', context)
	#return HttpResponse("Index")

def update_task(request, pk):
	instance = Task.objects.get(pk=pk)
	 
	if request.method == "POST":
		print("I ran")
		form = TaskForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
		return redirect('task:index')
	form = TaskForm(instance=instance)
	context = {
		'form': form
	}
	return render(request, 'task/update_task.html', context)

def delete_task(request, pk):
	task_object = get_object_or_404(Task, id=pk)
	if request.method == "POST":
		task_object.delete()
		return redirect('task:index')
	context	= {
		'task': task_object
	}
	return render(request, 'task/confirm_delete.html', context)
