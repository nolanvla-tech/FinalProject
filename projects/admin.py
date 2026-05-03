from django.contrib import admin
from .models import Project, Skill, Experience, SiteProfile


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    """Admin for portfolio owner's personal information."""
    list_display = ('name', 'title', 'email')
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'title', 'bio', 'profile_image')
        }),
        ('Contact', {
            'fields': ('email', 'phone')
        }),
        ('Social & Links', {
            'fields': ('github_url', 'linkedin_url', 'resume_file')
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin for portfolio projects."""
    list_display = ('title', 'category', 'is_featured', 'display_order', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'summary', 'description')
    ordering = ('display_order', '-created_at')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Project Basics', {
            'fields': ('title', 'summary', 'category', 'is_featured', 'display_order')
        }),
        ('Problem & Solution', {
            'fields': ('business_problem', 'description')
        }),
        ('Technical Details', {
            'fields': ('tools_used', 'key_features', 'your_role')
        }),
        ('Challenges & Learning', {
            'fields': ('biggest_challenge', 'lessons_learned')
        }),
        ('Media & Links', {
            'fields': ('featured_image', 'video_embed_url', 'github_url', 'demo_url'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin for skills."""
    list_display = ('name', 'category', 'proficiency', 'display_order')
    list_filter = ('category', 'proficiency')
    ordering = ('display_order',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """Admin for work experience and education."""
    list_display = ('title', 'company', 'experience_type', 'start_date', 'end_date')
    list_filter = ('experience_type', 'start_date')
    search_fields = ('title', 'company', 'description')
    ordering = ('-start_date',)
