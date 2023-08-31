from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TodoList
from .serializers import TodoListSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


class TodoListApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        queryset = TodoList.objects.all()
        serializer = TodoListSerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = TodoListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def todolist_detail(request, id):
    obj = get_object_or_404(TodoList, id=id)

    if request.method == 'GET':
        serializer = TodoListSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoListSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
