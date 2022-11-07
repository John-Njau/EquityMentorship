from django.shortcuts import render
from django.http import HttpResponse

from pictures.serializers import PictureSerializer
from pictures.models import Picture
# apiview
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PictureApiView(APIView):
    def get(self, request):
        pictures = Picture.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)