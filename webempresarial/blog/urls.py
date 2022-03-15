from django.urls import path
from . import views
urlpatterns = [

    
    path('',views.blog,name="blog"),
    # este path toma el parametro de la funcion category de views.py que es una cadena de caracteres que se parsea a entero mediante int:
    path('category/<int:category_id>/',views.category, name='category'),
]