from django.contrib import admin
from .models import Customer, Address,ContactInfo

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(ContactInfo)
