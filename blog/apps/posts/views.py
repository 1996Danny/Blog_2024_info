from django.shortcuts import render
from .models import Posts


# vista basada en funciones
def posts(request):
    ctx = {}  # contextos
    noticias = Posts.objects.all()  # select * from Posts
    ctx["noticias"] = noticias
    print(noticias)
    return render(request, "posts/posts.html", ctx)


def about_us(request):
    return render(request, "posts/about_us.html")


# vista basada en clase

from .form import RegistroForm
from django.views.generic import CreateView

# from django.urls import reverse_lazy


class Registro(CreateView):
    form_class = RegistroForm
    # success_url = reverse_lazy("noticia")
    template_name = "usuarios/registro.html"
