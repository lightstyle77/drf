from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from notes.views import NoteModelViewSet, ProjectModelViewSet
from users.views import UserCustomViewSet

router = DefaultRouter()  # Create a router
router.register('users', UserCustomViewSet)  # Register User model view set with the router
router.register('notes', NoteModelViewSet)  # Register Note model view set with the router
router.register('projects', ProjectModelViewSet)  # Register Project model view set with the router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # These urls are now determined automatically by the router
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
