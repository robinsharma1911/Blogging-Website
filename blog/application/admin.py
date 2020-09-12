from django.contrib import admin

from .models import Blog,Personal
# Register your models here.
admin.site.register(Blog) 
admin.site.register(Personal)
