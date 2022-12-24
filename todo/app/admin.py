from django.contrib import admin
from .models import Todo, Tag


class todoAdmin(admin.ModelAdmin):
    list_display = ['Timestamp','Title','Description','Due_Date','Status','get_tags']

admin.site.register(Todo, todoAdmin)
admin.site.register(Tag)
