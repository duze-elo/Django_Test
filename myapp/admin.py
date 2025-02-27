from django.contrib import admin
from .models import TodoList, TodoItem

# Register your models here.

# admin.site.register(TodoList)
# admin.site.register(TodoItem)

class TodoItemInline(admin.TabularInline):
    model = TodoItem
    extra = 1

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at',)
    inlines = [TodoItemInline]

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    item_display = ('title', 'todo_list', 'completed', 'created_at')
    search_fields = ('title', 'todo_list__title')
    list_filter = ('completed', 'created_at')