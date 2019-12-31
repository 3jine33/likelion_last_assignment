from rest_framework.routers import DefaultRouter
from django.urls import path, include
from storage import views

router = DefaultRouter()
router.register('essay', views.PostViewSet)
router.register('album', views.ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
