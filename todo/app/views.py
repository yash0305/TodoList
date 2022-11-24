from .models import Tag, Todo
from .serializers import TagSerializers, TodoSerializers
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from datetime import datetime

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def TagView(request):
    tasks = Tag.objects.all()
    s = TagSerializers(tasks, many=True)
    return Response(s.data)

@api_view(['GET'])
def taskList(request):
    tasks = Todo.objects.all()
    s = TodoSerializers(tasks, many=True)
    return Response(s.data)

@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Todo.objects.get(id = pk)
    s = TodoSerializers(tasks, many=False)
    return Response(s.data)

@api_view(['POST'])
def taskCreate(request):
    data = request.data
    t = data["Timestamp"]
    timeStamp = datetime.strptime(t[:10], "%Y-%m-%d")
    dueDate = datetime.strptime(data["Due_Date"], "%Y-%m-%d")
    if dueDate > timeStamp:
        new = TodoSerializers(data=data)
    else: 
        return Response("Due Date field value cannot be before Timestamp created")

    if new.is_valid():
        new.save()
    return Response(new.data)

@api_view(['PUT'])
def taskUpdate(request,pk):
    task = Todo.objects.get(id = pk)
    s = TodoSerializers(instance=task,data=request.data)
    if s.is_valid():
        s.save()
    return Response(s.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Todo.objects.get(id = pk)
    task.delete()
    return Response("Item succesfully deleted")

