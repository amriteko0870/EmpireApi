from pyexpat import model
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apiApp.models import storeData


class storeDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = storeData
        fields = ['id',
                  'store',
                  'sales',
                  'no_of_orders',
                  'no_of_customers']
                  