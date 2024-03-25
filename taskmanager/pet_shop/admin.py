from django.contrib import admin
from .models import Species, Pet, User


admin.site.register(Species)
admin.site.register(User)
admin.site.register(Pet)

