from django.contrib import admin
from.models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author', 'published','post_categories')
    # el ordering puede usar uno o mas campos siendo el mas prioritario el primero que se pone. En este ejemplo primero se ordena por autor y luego se ordena por la fecha de publicacion
    ordering = ('author','published')
    # el search_fields sirve para elementos que no estan enlazados con bases relacionales y buscan aquellos campos que esten adentro de la tupla. Para poder buscar campos que esten relacionados los datos se hace mediante __lugar-donde-este-ese-campo-relacionado
    search_fields = ('title','content','author__username','categories__name')
    # muestra un filtro de fechas dividido en el campo asignado
    date_hierarchy = 'published'
    #se hace un filtro por autor y por categorias
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        # el return devuelve una union de todas las categorias insertadas en el post ordenadas alfabateticamnete
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    
    # Renombra el nombre de la funcion post_categories por Categorias
    post_categories.short_description = "Categorias"


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)