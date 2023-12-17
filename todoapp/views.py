from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ToDo
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    TodoList = ToDo.objects.order_by('id')
    print(TodoList)
    context={'todolist':TodoList}
    return render(request,'todo/index.html',context)


def AddTodo(request):
    text = request.POST.get('text')
    todo=ToDo(text=text)
    todo.save()   
    return redirect('index')

def removeTodo(request,todo_id):
    todo= ToDo.objects.get(pk=todo_id)  
    todo.complete=True
    todo.save()
    return redirect('index')

def deleteCopleted(request):
    todo=ToDo.objects.filter(complete=True).delete()
    return redirect("index")

def deleteAll(request):
    todo=ToDo.objects.all().delete()
    return redirect("index")




