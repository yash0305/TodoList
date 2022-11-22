from rest_framework.viewsets import ModelViewSet
from .models import Tag, Todo
from .serializers import TagSerializers, TodoSerializers
from rest_framework.response import Response

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers