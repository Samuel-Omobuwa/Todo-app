from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializers):
    class Meta:
        model = Todo
        field = ('id', 'title', 'description', 'completed')