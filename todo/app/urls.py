from rest_framework.routers import DefaultRouter
from .views import TagViewSet, TodoViewSet

app_name = 'app'

router = DefaultRouter()

router.register('tag', TagViewSet, basename='tag')
router.register('todo', TodoViewSet, basename='todo')

urlpatterns = router.urls

