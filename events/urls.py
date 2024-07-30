from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, TimezoneListView

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = []
