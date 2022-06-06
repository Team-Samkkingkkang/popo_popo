import Generics as Generics
from rest_framework import generics
from rest_framework.pagination import PageNumberPegination


class PostPagination(PageNumberPegination):
    page_size = 10


class PostListAPIView(Generics.ListAPIView):  # CBV
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination


urlpatterns = [
    path('posts/', PostListApiView.as_view(), anme='post_list'),
]