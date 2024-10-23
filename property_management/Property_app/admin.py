from django.contrib import admin
from django.contrib import admin


from .models import Property,Tenant,Unit,Lease
admin.site.register(Property)
admin.site.register(Tenant)
admin.site.register(Unit)
admin.site.register(Lease)
# Register your models here.
