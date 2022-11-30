from rest_framework import serializers
from .models import Tag, Todo
from django.db.models.functions import Now
from django.db import models


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TodoSerializers(serializers.ModelSerializer):
    Tag = TagSerializers(many=True)
    class Meta:
        model = Todo
        fields = '__all__'
        constraints = [
        models.CheckConstraint(
            check=models.Q(Date_Now=Now()),
            name='created_at_cannot_be_past_date'
        )
    ]         