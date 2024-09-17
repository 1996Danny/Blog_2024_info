from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Categorias(models.Model):  # nombreapp_nombreclase
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Posts(models.Model):  # nombreapp_nombreclase
    titulo = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Titulo"
    )
    contenido = models.TextField(verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    class Meta:
        db_table = "Posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo
