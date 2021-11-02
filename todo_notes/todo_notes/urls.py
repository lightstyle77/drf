from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from notes.views import NoteModelViewSet, ProjectModelViewSet
from users.views import UserModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('notes', NoteModelViewSet)
router.register('projects', ProjectModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
