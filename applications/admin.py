from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("company_name", "role", "status", "location", "updated_at")
    list_filter = ("status", "location")
    search_fields = ("company_name", "role", "notes")
