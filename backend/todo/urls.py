from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("api/todo", views.TodoViewSet, basename="todo")
urlpatterns = [
    router.urls
]
