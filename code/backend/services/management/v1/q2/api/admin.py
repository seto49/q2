from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'reference',
        'active',
        'created_at',
        'last_modified_at',
    ]

admin.site.register(Link, LinkAdmin)
