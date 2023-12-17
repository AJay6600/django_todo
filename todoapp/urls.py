
from django.urls import path,include
from todoapp import views

urlpatterns = [
    path('',views.index ,name='index'),
    path('add/',views.AddTodo, name="addtodo"),
    path("remove/<todo_id>",views.removeTodo,name="removeTodo"),
    path("delete/completed/",views.deleteCopleted,name="delete completed"),
    path("delete/all/",views.deleteAll,name="delete all")
    

]
