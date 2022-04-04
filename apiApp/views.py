from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.contrib.auth.hashers import make_password,check_password

from apiApp.models import storeData, user , graph
from apiApp.serializers import storeDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
# Create your views here.
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from apiApp.models import storeData
from apiApp.serializers import storeDataSerializer,graphSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
def index(request,format=None):
    if request.method == 'GET':
        try:
            data = storeData.objects.all()
            data_serializer = storeDataSerializer(data, many=True)
            print(data_serializer)
            return JsonResponse(data_serializer.data, safe=False)

        except:
            return Response({'Message':'No Data Available'})

    if request.method == 'POST':
        data1 = request.data
        try:
            storeData.objects.filter(store=data1.get('store'))
            return Response({'Message':'Store Already Exist'})
        except:
            storeData.objects.create(
                                    store = data1.get('store'),
                                    sales = data1.get('sales'),
                                    no_of_orders = data1.get('no_of_orders'),
                                    no_of_customers = data1.get('no_of_customers')
                                    )

            return Response({'Data Saved': request.data})
    if request.method == 'PUT':
        data1 = request.data
        if(data1.get('id')==None or data1.get('store')==None or data1.get('sales')==None or data1.get('no_of_customers')==None or data1.get('no_of_orders')==None):
            return Response({'Message': 'Invalid Data'})
        else:
            storeData.objects.filter(id=data1.get('id')).update(
                                                                store=data1.get('store'),
                                                                sales=data1.get('sales'),
                                                                no_of_customers=data1.get('no_of_customers'),
                                                                no_of_orders=data1.get('no_of_orders')
                                                                )
            return Response({'data updated': request.data})

@api_view(['GET'])
def api_test_50(request,format=None):   
    if request.method == 'GET':
        try:
            data = graph.objects.all()
            data_serializer = graphSerializer(data, many=True)
            return JsonResponse(data_serializer.data, safe=False)

        except:
            return Response({'Message':'No Data Available'})
