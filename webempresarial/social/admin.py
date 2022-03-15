from django.contrib import admin
from .models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

    # lo que hace esto es filtrar los campos de lectura en el caso de un usuario tiene el rol de Personal
    # que no accede a todas las propiedades del superusuario
    def get_readonly_fields(self, request, obj:None):
        if request.user.groups.filter(name = 'Personal').exists():
            return ('key','name')
        else:
            return ('created','updated')



admin.site.register(Link, LinkAdmin)