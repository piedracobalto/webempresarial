from django.contrib import admin
from .models import Service 

# Register your models here.

# el usuario es pcg1, el mail es pedro@hotmail.com y el password es hola1234

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Service, ServiceAdmin)

