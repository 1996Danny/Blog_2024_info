from django.shortcuts import render
from .models import Posts, User


# vista basada en funciones
def posts(request):
    ctx = {}  # contextos
    noticias = Posts.objects.all().order_by("-id")  # select * from Posts
    ctx["noticias"] = noticias

    return render(request, "posts/posts.html", ctx)


def post_id(request, id):
    ctx = {}
    noticia = Posts.objects.get(id=id)
    ctx["noticia"] = noticia
    return render(request, "posts/detalle.html", ctx)


def about_us(request):
    return render(request, "posts/about_us.html")


def perfil(request, id):
    ctx = {}
    usuarios = User.objects.get(id=id)
    ctx["usuarios"] = usuarios
    print(usuarios)
    return render(request, "usuarios/perfil.html", ctx)


# vista basada en clase

from .form import RegistroForm, CrearForm, ModificarForm
from django.views.generic import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("noticias")
    template_name = "usuarios/registro.html"


class CrearPost(CreateView):
    form_class = CrearForm
    model = Posts
    template_name = "posts/crear_post.html"
    success_url = reverse_lazy("noticias")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class EliminarPost(DeleteView):
    model = Posts
    success_url = reverse_lazy("noticias")


class ModificarPost(UpdateView):
    model = Posts
    form_class = ModificarForm
    template_name = "posts/modificar_post.html"
    success_url = reverse_lazy("noticias")
