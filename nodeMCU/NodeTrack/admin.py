from django.contrib import admin
from .models import Person

# Registrar Person no banco ADMIN
admin.site.register(Person)
