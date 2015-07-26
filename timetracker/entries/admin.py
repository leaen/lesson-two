from django.contrib import admin

# Register your models here.
from . import models

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('client', 'name')
    list_filter = ('client',)
    search_fields = ('client', 'name')

class WorkPeriodAdmin(admin.ModelAdmin):
    list_display = ('start', 'stop')

class EntryAdmin(admin.ModelAdmin):
    list_display = ('project', 'description', 'workPeriod')
    list_filter = ('project',)
    search_fields = ('project', 'description',)

admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.WorkPeriod, WorkPeriodAdmin)
admin.site.register(models.Entry, EntryAdmin)
