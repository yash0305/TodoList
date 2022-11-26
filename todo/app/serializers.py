from rest_framework import serializers
from .models import Tag, Todo

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TodoSerializers(serializers.ModelSerializer):
    Tag = TagSerializers(many=True)
    class Meta:
        model = Todo
        fields = '__all__'