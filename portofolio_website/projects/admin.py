from django.contrib import admin

# Register your models here.
from .models import projects, category

admin.site.register(projects)
admin.site.register(category)