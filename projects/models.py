from django.db import models
from django.utils import timezone

class SiteProfile(models.Model):
    """
    Store portfolio owner's personal information.
    """
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300, help_text="Your professional title/headline")
    bio = models.TextField(help_text="Your professional biography (2-3 sentences)")
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)
    
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    
    resume_file = models.FileField(upload_to='resume/', null=True, blank=True, help_text="PDF resume")
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Site Profile"
        verbose_name_plural = "Site Profile"


class Project(models.Model):
    """
    Model to store portfolio projects with comprehensive details.
    """
    
    CATEGORY_CHOICES = [
        ('chatbot', 'Chatbot Project'),
        ('n8n_automation', 'n8n Automation Workflow'),
        ('langchain_agent', 'LangChain Agent'),
        ('ml_project', 'Machine Learning Project'),
        ('django_app', 'Django Web Application'),
        ('google_ai', 'Google AI Studio Project'),
        ('other', 'Other'),
    ]
    
    # Basic Info
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500, help_text="One-sentence summary of the project")
    
    # Detailed Content
    business_problem = models.TextField(help_text="What problem does this solve?")
    description = models.TextField(help_text="Full project description")
    
    # Technical Details
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    tools_used = models.CharField(max_length=500, help_text="Comma-separated: Python, Django, etc.")
    
    key_features = models.TextField(help_text="Key features (one per line)")
    your_role = models.TextField(help_text="Your specific role and contributions")
    
    # Challenges & Learning
    biggest_challenge = models.TextField(help_text="What was your biggest challenge?")
    lessons_learned = models.TextField(help_text="What did you learn from this project?")
    
    # Media & Links
    featured_image = models.ImageField(upload_to='projects/', null=True, blank=True)
    video_embed_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)
    
    # Metadata
    is_featured = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0, help_text="Order of display (lower = first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.title


class Skill(models.Model):
    """
    Store technical and professional skills.
    """
    
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=[
            ('technical', 'Technical'),
            ('business', 'Business'),
            ('soft', 'Soft Skills'),
            ('language', 'Language'),
        ],
        default='technical'
    )
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='intermediate')
    description = models.CharField(max_length=300, blank=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return self.name


class Experience(models.Model):
    """
    Store work experience and education.
    """
    
    EXPERIENCE_TYPE = [
        ('work', 'Work Experience'),
        ('education', 'Education'),
        ('leadership', 'Leadership'),
    ]
    
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_TYPE, default='work')
    
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank for current role")
    
    description = models.TextField(help_text="Job description and achievements (one per line)")
    
    display_order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date', 'display_order']
    
    def __str__(self):
        return f"{self.title} at {self.company}"
