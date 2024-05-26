from song_app.models import Song
from song_app.serializers import SongSerializer, PartialUpdateSerializer
from song_app.helpers import BaseCustomModelViewSet
from song_app.config import PAGE_SIZE

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination



class CustomPagination(PageNumberPagination):
    page_size = PAGE_SIZE

class SongViewSet(BaseCustomModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    pagination_class = CustomPagination
    http_method_names = ["get", "patch"]

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return PartialUpdateSerializer
        return SongSerializer