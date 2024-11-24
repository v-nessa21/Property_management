from django.urls import path

from .views import list_lease, list_tenant, list_properties1, list_unit1, list_lease1,property_list, \
    list_unit

urlpatterns = [

    path('', property_list, name='list_properties'),

    path('1/', list_unit, name='list_unit'),

    path('2/', list_lease, name='list_lease'),

    path('3/', list_tenant, name='list_tenant'),

    path('4/', list_properties1, name='list_tenant'),

    path('5/', list_unit1, name='list_tenant'),

    path('6/', list_lease1, name='list_tenant'),


]
