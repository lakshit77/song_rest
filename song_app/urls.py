from django.urls import path, include
from rest_framework.routers import DefaultRouter
from song_app.views import SongViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('songs', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)