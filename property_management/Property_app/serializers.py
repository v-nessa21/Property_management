from rest_framework import serializers
from .models import Property, Unit, Tenant, Lease

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id','my_name','address','property_type','description','number_of_units']

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'property_id','unit_number','bedrooms','bathrooms','rent','is_available']

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id','name','email','phone_number']

class LeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lease
        fields = ['id','tenant_id','unit_id','start_date','end_date','rent_amount']
