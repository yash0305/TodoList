# from rest_framework.routers import DefaultRouter
# from .views import TagViewSet, TodoViewSet

# app_name = 'app'

# router = DefaultRouter()

# router.register('tag', TagViewSet, basename='tag')
# router.register('todo', TodoViewSet, basename='todo')

# urlpatterns = router.urls

from django.urls import path

from .views import TagView, taskList, taskDetail, taskCreate, taskDelete, taskUpdate, tagCreate

urlpatterns = [
    path('tag', TagView, name='tag'),
    path('tag-create/', tagCreate, name='tag-create'),
    path('todo-list/', taskList, name='todo-list'),
    path('todo-detail/<str:pk>/', taskDetail, name="todo-detail"),
	path('todo-create/', taskCreate, name="todo-create"),

	path('todo-update/<str:pk>/', taskUpdate, name="todo-update"),
	path('todo-delete/<str:pk>/', taskDelete, name="todo-delete"),
    
]

