from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from http import HTTPStatus as status

from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def get_all_post(request):
    queryset = Post.objects.all()
    if queryset.exists():
        serializer_all = PostSerializer(queryset, many=True)
        return Response(serializer_all.data)
    return Response(status=status.HTTP_400_NOT_FOUND)

@api_view(['GET'])
def filter_post_by_id(request, id):
    queryset = Post.objects.filter(id=id)
    if queryset.exists():
        serializer_all = PostSerializer(queryset, many=True)
        return Response(serializer_all.data)
    return Response(status=status.HTTP_400_NOT_FOUND)

@api_view(['POST'])
def add_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_ERROR_ON_CREATE)