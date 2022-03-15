from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'Nombre')
    created = models.DateTimeField (auto_now_add= True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField (auto_now= True, verbose_name= "Fecha de edicion")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name= 'Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicacion',default=now)

    # se pone 'null=True' y 'blank=True' para que no sea obligatorio subir una imagen en un posteo.
    image = models.ImageField(verbose_name='Imagen', upload_to = 'blog', null=True, blank=True)

    #se pone on_delete=models.CASCADE para que en el momento que se borre el autor, se borre los posteos
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name="get_posts")
    created = models.DateTimeField (auto_now_add= True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField (auto_now= True, verbose_name= "Fecha de edicion")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title