from django.contrib import admin
from .models import MagicSquare


class MagicSquareAdmin(admin.ModelAdmin):
    list_display = ('id', 'hint')


admin.site.register(MagicSquare, MagicSquareAdmin)
