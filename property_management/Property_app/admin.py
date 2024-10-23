from django.contrib import admin
from django.contrib import admin


from .models import Property,Tenant,Unit,Lease
admin.site.register(Property)    # property
admin.site.register(Tenant)      # tenant
admin.site.register(Unit)        # unit
admin.site.register(Lease)       # lease

# Register your models here.
