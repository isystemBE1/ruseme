from django.contrib import admin
from .models import Services, Projects, Category

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession')
    search_fields = ('profession',)
    list_filter = ('id', 'profession')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    search_fields = ('category',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession')
    search_fields = ('profession', 'category')
    list_filter = ('profession',)


admin.site.register(Services, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Projects, ProjectAdmin)
