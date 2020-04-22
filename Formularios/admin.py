from django.contrib import admin

# Register your models here.
from .models import Pregunta, Alternativa

admin.site.register(Pregunta)
admin.site.register(Alternativa)
