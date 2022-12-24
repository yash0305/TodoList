from rest_framework import serializers
from .models import Tag, Todo
from django.db.models.functions import Now
from django.db import models


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TodoSerializers(serializers.ModelSerializer):
    # Tag = TagSerializers(many=True)
    Tag = serializers.StringRelatedField(many=True)
    class Meta:
        model = Todo
        fields = '__all__'
       




       