from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from GRsystem.views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GRsystem.urls')),
    path('api/', include(router.urls)),
    path('communication/', include('communication.urls')),
    # Add other URL patterns here if needed
]
