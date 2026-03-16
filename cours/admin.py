from django.contrib import admin

# Register your models here.
from .models import Enseignant, Cours
admin.site.register(Enseignant)
admin.site.register(Cours)