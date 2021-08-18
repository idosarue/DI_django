from django.urls import path
from . import views
urlpatterns = [
    path('add_todo', views.todo),
    path('display_todo', views.display_todos, name='display_todo'),
    path('done/<int:id>', views.done, name='done'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
]
