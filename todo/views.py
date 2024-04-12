from django.http import HttpResponse
from rest_framework import permissions, viewsets
from django.core import serializers
from rest_framework.permissions import IsAuthenticated
from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        todo = Todo.objects.create(
            title=request.POST.get('title', ''),
            description=request.POST.get('description', ''),
            user=request.user
        )
        serialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serialized_obj, content_type='application/json')
