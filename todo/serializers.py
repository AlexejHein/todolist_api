from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'created_at']