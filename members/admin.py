from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "approved"]
    list_editable = ["approved"]
    list_filter = ["approved"]
    ordering = ["approved"]


admin.site.register(Profile, ProfileAdmin)