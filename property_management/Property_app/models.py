from django.db import models
from django.db import models

# Create your models here.

Property_type = (
    ('Apartment', 'Apartment'),
    ('commercial', 'Commercial'),
    ('house', 'House'),
)
#property model
class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100, choices=Property_type)
    description = models.TextField()
    number_unit = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#unit property
class Unit(models.Model):
    property_type = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    rent = models.IntegerField()
    is_available = models.BooleanField()
    def __str__(self):
        return self.unit_number
#tenant model
class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    def __str__(self):
        return self.email
#lease model
class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.IntegerField()
    def __str__(self):
        return self.tenant.name


