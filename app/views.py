from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import ImageRecognitionSerializer

import os
from .Model.classify import classify

# def index(request):
#     return HttpResponse("Hello World")

class ImageRecognition(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ImageRecognitionSerializer(data=request.data)


        if serializer.is_valid():    
            serializer.save()
            data = serializer.data
            print(data)
            path = str(os.getcwd()) + "/static/media/" + str(data["file"][7:])
            percentages = []
            percentages = classify(path)
            if(len(percentages) == 0):
                percentages.append("notworking")
            
            return Response(percentages, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)