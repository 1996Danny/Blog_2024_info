# urls solo de la app posts
from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts, name="noticias"),
    path("about/", views.about_us, name="about"),
    path("registro/", views.Registro.as_view(), name="registro"),
]
