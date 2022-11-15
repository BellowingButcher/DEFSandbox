from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response

class TodoAPIView(APIView):
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get_all_objects(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = TodoSerializer(data)

        else:
            data = Todo.objects.all()