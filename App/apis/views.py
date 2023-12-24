from django.shortcuts import render
from rest_framework import generics, permissions
from blog.models import Post
from .serializers import BlogSerializer
from .permissions import IsAuthorOrReadOnly
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def postCreate(request):
    serializer = BlogSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


class BlogAPIView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
