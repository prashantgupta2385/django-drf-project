from django.urls import path
from .views import CreateTodoAPIView,TodoListAPIView,TodoDetailAPIView

urlpatterns=[
    path('create',CreateTodoAPIView.as_view(),name="create-todo"),
    path('list',TodoListAPIView.as_view(),name="list-todo"),
    path("<int:id>",TodoDetailAPIView.as_view(),name="todo")
]