from django.contrib import admin

# Register your models here.
from .models import Projects,Profile

admin.site.register(Projects)
admin.site.register(Profile)
