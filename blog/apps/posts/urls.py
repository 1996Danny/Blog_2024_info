# urls solo de la app posts
from django.urls import path
from . import views

urlpatterns = [
    # vbf
    # path("", views.posts, name="noticias"),
    # vbc
    path("", views.Noticias.as_view(), name="noticias"),
    path("about/", views.about_us, name="about"),
    path("registro/", views.Registro.as_view(), name="registro"),
    path("detalle/<int:id>", views.post_id, name="detalle"),
    # crear nuevo post
    path("nuevo_post/", views.CrearPost.as_view(), name="nuevo_post"),
    # eliminar
    path("eliminar/<int:pk>", views.EliminarPost.as_view(), name="eliminar_post"),
    # modificar
    path("modificar/<int:pk>", views.ModificarPost.as_view(), name="modificar_post"),
    # perfil del usuario
    path("perfil/<int:id>", views.perfil, name="perfil"),
    # url de comentario
    path("comentar/", views.comentar_post, name="comentar"),
    path(
        "borrar/<int:pk>", views.EliminarComentario.as_view(), name="borrar_comentario"
    ),
    path(
        "modificar_com/<int:pk>",
        views.ModificarComentario.as_view(),
        name="modificar_comentario",
    ),
]
