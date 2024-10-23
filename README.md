Django-assignment-property_management 
UNIVERSTY OF RWANDA
COLLEGE OF SCIENCE AND TECHNOLOGY
YEAR THREE
DEPARTMENT OF INFORMATION TECHNOLOGY
COLLABORATORS:
uwase jeanne vanessa      222 014 572
Irahari Hussein           222 012 293

This is the property managemementwhich is composed of property_app(models,view,admin,setting)

so in the beginning we created the virtual environment 


installed the pip Django


run the initial migration 

create the super user with their credentials




run the server

accessing the admin interface

Models overview

.1.Property model

represent a property(e.g apartment complex,commercialbuilding).key fields:

name:name of the proprty.

address:physics address of the property.

property_type:type of property(e.g:apartment,house,commercial).


description:additionaldescription or notes about the property.

number-of_units:number of units available in the property

.2. unit model
   
it represents the following key fields

property:foreighnkey to the property model.

unit_number:identifier for the unit

bedrooms,bathrooms:number of bedrooms and barhrooms.

rent:monthly rent for the unit.

is_available for lease.

.3. tenant model

represents a tents in the property management system. key fields:

name:tenant' full name

email:tenant'email addess

phone_number: tenant's phone number

.4.lease model

represents a lease agreements between a tenant and a unit. key fields:

tenant:foreignkey to the tenant model

unit:foreignkey to the unit model

start-data,end_date:dates when the lease starts and ends.

rent_amount:rent amount agrees upon in the lease


IN THE ADMIN INTERFACE

so when running the server and go to ADMIN INTERFACE you can login using credentials of super user here the admin is allowed to add an information in same property management 


Admin is allowed to add ,change and delete all information 


