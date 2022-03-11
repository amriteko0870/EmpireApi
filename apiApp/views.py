from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from apiApp.models import storeData
from apiApp.serializers import storeDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def index(request,format=None):
    if request.method == 'GET':
        data = storeData.objects.all()
        data_serializer = storeDataSerializer(data, many=True)
        print(data_serializer)
        return JsonResponse(data_serializer.data, safe=False)

    if request.method == 'POST':
        data1 = request.data
        #storeData.objects.create(
        #                        store = data1.get('store'),
        #                         sales = data1.get('sales'),
        #                         no_of_orders = data1.get('no_of_orders'),
        #                         no_of_customers = data1.get('no_of_customers')
        #                         )
        
        return Response({'Data Saved': request.data})