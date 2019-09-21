from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from django.utils.safestring import mark_safe

from . import models


class Test_insAdmin(admin.ModelAdmin):
    def affiche_image(self, obj):
        if obj.image :
            return mark_safe('<img src="{url}" width="100" height="100" > </img>'.format(url = obj.image.url))
        else:
            return 'null'

    list_display = ('affiche_image','id', 'nom', 'prenom', 'email')
    list_filter = ('id', 'nom', 'prenom', 'email')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Test_ins, Test_insAdmin)
