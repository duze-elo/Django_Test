from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="todos"),
    path("todos/create/", views.create_todo_list, name="todo_create"),
    path("todos/list/delete/<int:list_id>/", views.delete_todo_list, name="delete_todo_list"),
    path('todos/item/delete/<int:item_id>/', views.delete_todo_item, name='delete_todo_item'),

]