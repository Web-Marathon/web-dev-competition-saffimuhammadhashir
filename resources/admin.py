# admin.py

from django.contrib import admin
from .models import ResourcePost

@admin.register(ResourcePost)
class ResourcePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'body', 'user')
        }),
    )

    readonly_fields = ('user', 'created_at')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)
