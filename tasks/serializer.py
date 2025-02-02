from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data.setdefault("index", 0)
        return super().create(validated_data)