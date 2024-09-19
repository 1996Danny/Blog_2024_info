from django.contrib import admin
from .models import Posts, Categorias, User

# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    search_fields = ("titulo",)
    list_filter = ["categoria", "autor__username"]
    list_display = ["titulo", "autor", "categoria"]
    date_hierarchy = "fecha_publicacion"


admin.site.register(Posts, PostsAdmin)
admin.site.register(Categorias)
admin.site.register(User)
