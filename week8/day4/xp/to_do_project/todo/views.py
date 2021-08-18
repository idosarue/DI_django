from django.db.models.fields import DateField, DateTimeField
from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from .forms import TodoForm
from .models import Category, Todo
from datetime import datetime
# Create your views here.
def todo(request):
    if request.method == 'GET':
        form = TodoForm()
    elif request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Todo.objects.create(**form.cleaned_data)
            return redirect('display_todo')
    return render(request, 'add_todo.html', {'form':form})


def display_todos(request):
    f = Todo.objects.all()
    return render(request, 'display_todo.html', {'details':f})

def done(request, id):
    f = get_object_or_404(Todo, id=id)
    f.has_been_done = True
    f.date_completion = datetime.now()
    f.save()
    return redirect('display_todo') 

def delete_task(request, id):
    f = get_object_or_404(Todo, id=id)
    f.delete()
    return redirect('display_todo') 

