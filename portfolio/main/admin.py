from django.contrib import admin
from django.utils.html import format_html
from .models import SiteProfile, Skill, Project, ContactMessage


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'email', 'profile_preview']
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'role', 'email', 'about_text')
        }),
        ('Media', {
            'fields': ('profile_image', 'resume_file'),
            'description': 'Upload your profile picture and resume PDF here.'
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url')
        }),
    )

    def profile_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" style="width:50px;height:50px;border-radius:50%;object-fit:cover;">', obj.profile_image.url)
        return "No image"
    profile_preview.short_description = "Profile"

    def has_add_permission(self, request):
        return not SiteProfile.objects.exists()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'percentage', 'order', 'skill_bar']
    list_editable = ['percentage', 'order']
    list_filter = ['category']
    ordering = ['category', 'order']

    def skill_bar(self, obj):
        return format_html(
            '<div style="width:200px;background:#1e293b;border-radius:4px;height:12px;">'
            '<div style="width:{}%;background:linear-gradient(90deg,#38bdf8,#6366f1);height:100%;border-radius:4px;"></div>'
            '</div>',
            obj.percentage
        )
    skill_bar.short_description = "Level"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order', 'screenshot_preview', 'created_at']
    list_editable = ['featured', 'order']
    list_filter = ['category', 'featured']
    search_fields = ['title', 'description', 'tags']
    fieldsets = (
        ('Project Info', {
            'fields': ('title', 'description', 'short_description', 'category', 'tags', 'featured', 'order')
        }),
        ('Media', {
            'fields': ('screenshot',)
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
    )

    def screenshot_preview(self, obj):
        if obj.screenshot:
            return format_html('<img src="{}" style="width:80px;height:50px;object-fit:cover;border-radius:4px;">', obj.screenshot.url)
        return "No image"
    screenshot_preview.short_description = "Preview"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'submitted_at', 'is_read']
    list_filter = ['is_read', 'submitted_at']
    list_editable = ['is_read']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'submitted_at']

    def has_add_permission(self, request):
        return False


# Customize admin site
admin.site.site_header = "Dhanunjaya Reddy — Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Dashboard"
