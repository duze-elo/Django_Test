from django.shortcuts import render
from .models import TodoItem, TodoList
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required
def todos(request):
    user = request.user
    lists = TodoList.objects.filter(user=user)
    items = TodoItem.objects.filter(todo_list__in=lists)
    return render(request, "todos.html", {"todos": items, "lists": lists})