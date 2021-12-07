from django.contrib import admin
from core.models import Entregadore, Parceiro


admin.site.register(
    [
        Entregadore,
        Parceiro
    ]
)
