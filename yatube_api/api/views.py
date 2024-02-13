from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets

from posts.models import Group, Post
from .serializers import CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_post_object(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post_object().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post_object())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FollowSerializer

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return self.get_object().following_users.all()

    def perform_create(self, serializer):
        serializer.save(user=self.get_object())
