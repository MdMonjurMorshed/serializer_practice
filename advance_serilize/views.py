from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import  Response
from advance_serilize.serializer import CreateFirstSerializer
from advance_serilize.models import FirstModel,Publisher
from advance_serilize.serializer import PublisherModelSerializer
from rest_framework import status

# Create your views here.
class CreateFist(APIView): 
    def post(self,request,*args,**kwargs): 
        data=request.data
        serializer=CreateFirstSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            FirstModel.objects.create(
                title=serializer.validated_data.get('title')
            )
            return Response ({"message":"data is saved successfully"},status=status.HTTP_201_CREATED)
        
       
        return Response ({"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class GetAllPublisher(APIView):
    def get(slef,request,*args,**kwargs):
        queryset=Publisher.objects.all().prefetch_related('books')
        if queryset:
            serializer=PublisherModelSerializer(queryset,many=True)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'message':'No data found'},status=status.HTTP_400_BAD_REQUEST)
