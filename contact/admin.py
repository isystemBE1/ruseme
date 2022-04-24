from django.contrib import admin
from .models import GitIntouch


# Register your models here.

class GitIntouchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name',)


admin.site.register(GitIntouch, GitIntouchAdmin)