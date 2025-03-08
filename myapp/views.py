from django.shortcuts import render, redirect, get_object_or_404
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

@login_required
def todo_create(request):
    return render(request, "todo_create.html")

@login_required
def create_todo_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        todo_list = TodoList.objects.create(user=request.user, title=title)

        index = 0
        while f"item_{index}_title" in request.POST:
            item_title = request.POST.get(f"item_{index}_title").strip()
            completed = request.POST.get(f"item_{index}_completed") == "true"

            if item_title:
                TodoItem.objects.create(
                    todo_list=todo_list,
                    title=item_title,
                    completed=completed
                )

            index += 1

        return redirect("todos")

    return render(request, "todo_create.html")



@login_required
def delete_todo_list(request, list_id):
    todo_list = get_object_or_404(TodoList, id=list_id, user=request.user)
    todo_list.delete()
    return redirect('todos')

@login_required
def delete_todo_item(request, item_id):
    todo_item = get_object_or_404(TodoItem, id=item_id, todo_list__user=request.user)
    todo_item.delete()
    return redirect('todos')
