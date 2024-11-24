from django.db import models
# Create your models here.
property_type = (
    ('commercial', 'commercial'),
    ('residential', 'residential'),
    ('apartment', 'apartment')
)
class Property(models.Model):

    my_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100, choices=property_type)
    description = models.TextField(default='',)
    number_of_units = models.IntegerField(default=0)

    def _str_(self):
        return f'{self.my_name} is located in {self.address}'
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    rent = models.IntegerField()
    is_available = models.BooleanField()
    def _str_(self):
        return f'{self.unit_number} {self.is_available}'
    #
    # {self.bedrooms} {self.bathrooms} {self.rent} {self.is_available}

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    def _str_(self):
         return f'{self.name}'
     # {self.email} {self.phone_number}

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.IntegerField()
    def _str_(self):
        return self.tenant.name
