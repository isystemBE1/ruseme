from django.contrib import admin
from .models import About, Tag, Resume

# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth', 'zip_code')
    filter_horizontal = ('tag',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_finish', 'academy', 'profession', 'created_at')
    list_filter = ('id', 'created_at')
    search_fields = ('academy', 'profession')


admin.site.register(About, AboutAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Resume, ResumeAdmin)
