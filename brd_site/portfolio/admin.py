from django.contrib import admin

from .models import Content, Project, TechTag

admin.site.register(Content)
admin.site.register(Project)
admin.site.register(TechTag)
