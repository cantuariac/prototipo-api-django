from django.contrib import admin
from .models import Profile, Registro
from django.contrib.auth import models

admin.site.register(Registro)
admin.site.register(Profile)