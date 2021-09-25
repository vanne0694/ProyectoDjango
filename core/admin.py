from django.contrib import admin
from .models import Person, Store, Client

# Register your models here.
admin.site.register(Person)
admin.site.register(Store)
admin.site.register(Client)
