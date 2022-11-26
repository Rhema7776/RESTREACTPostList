from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostListView(generics.ListAPIView):
    permission_classes = [permission.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer