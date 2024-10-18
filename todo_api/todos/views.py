from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import TodoSerializer
from .models import Todo
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
class CreateTodoAPIView(CreateAPIView):
    # this interanly only implement post request
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,)
   
    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)

class TodoListAPIView(ListAPIView):
    # this interanly only implement get request
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,)
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]

    filterset_fields=['id','title','desc','is_complete']
    search_fields=['id','title','desc','is_complete']
    ordering_fields=['id','title','desc','is_complete']
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field='id'
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)