from rest_framework import viewsets
from .models import Essay, Album
from .serializers import EssaySerializer, AlbumSerializer
from rest_framework.filters import SearchFilter

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fileds = ('title', 'body')

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer