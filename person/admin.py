from django.contrib import admin
from .models import About, Partner, Resume, Skill


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth', 'zip_code')


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


class ResumeAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    list_display = ('id', 'start_finish', 'academy', 'profession', 'created_at')
    list_filter = ('id', 'created_at')
    search_fields = ('academy', 'profession')


admin.site.register(About, AboutAdmin)
admin.site.register(Partner)
admin.site.register(Resume, ResumeAdmin)
