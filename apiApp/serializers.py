from pyexpat import model
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apiApp.models import storeData,graph


class storeDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = storeData
        fields = ['id',
                  'store',
                  'sales',
                  'no_of_orders',
                  'no_of_customers']

class graphSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = graph
        fields = [
            'dates',
            'sales',
            'profits',
            'tax',
            'discount',
            'expected',
            'o_chan',
            'deposit',
            'orders'
        ]
                  