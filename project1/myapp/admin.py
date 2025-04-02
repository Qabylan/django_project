from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at') # Поля, которые будутотображаться в списке
    search_fields = ('title',) # Поиск по названию задачи
    ist_filter = ('created_at',) # Фильтр по дате создания