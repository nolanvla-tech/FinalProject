from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Project, Skill, Experience, SiteProfile


def get_site_profile():
    """Get site profile, preferring the one with data."""
    # Try to get the profile with name first (most likely to be the real one)
    profile = SiteProfile.objects.filter(name__isnull=False).exclude(name='').first()
    
    # If no profile with name, get the first one
    if not profile:
        profile = SiteProfile.objects.first()
    
    # If still no profile, create a default one
    if not profile:
        profile, created = SiteProfile.objects.get_or_create(id=1)
    
    return profile


def home(request):
    """Homepage with hero section and featured projects."""
    profile = get_site_profile()
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    recent_projects = Project.objects.all()[:6]
    
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'recent_projects': recent_projects,
    }
    return render(request, 'projects/home.html', context)


def about(request):
    """About page with bio and key accomplishments."""
    profile = get_site_profile()
    experiences = Experience.objects.all()
    
    context = {
        'profile': profile,
        'experiences': experiences,
    }
    return render(request, 'projects/about.html', context)


def projects_list(request):
    """Display all portfolio projects."""
    projects = Project.objects.all()
    
    # Filter by category if provided
    category = request.GET.get('category')
    if category:
        projects = projects.filter(category=category)
    
    context = {
        'projects': projects,
        'categories': Project.CATEGORY_CHOICES,
    }
    return render(request, 'projects/projects_list.html', context)


def project_detail(request, pk):
    """Display individual project detail page."""
    project = get_object_or_404(Project, pk=pk)
    related_projects = Project.objects.filter(
        category=project.category
    ).exclude(pk=pk)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'projects/project_detail.html', context)


def skills(request):
    """Display all skills organized by category."""
    technical_skills = Skill.objects.filter(category='technical')
    business_skills = Skill.objects.filter(category='business')
    soft_skills = Skill.objects.filter(category='soft')
    languages = Skill.objects.filter(category='language')
    
    context = {
        'technical_skills': technical_skills,
        'business_skills': business_skills,
        'soft_skills': soft_skills,
        'languages': languages,
    }
    return render(request, 'projects/skills.html', context)


def resume(request):
    """Display resume/CV page."""
    profile = get_site_profile()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'skills': skills,
    }
    return render(request, 'projects/resume.html', context)


def contact(request):
    """Display contact page with form."""
    profile = get_site_profile()
    
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # TODO: Send email using Django email backend
        # For now, just redirect to success page
        return render(request, 'projects/contact_success.html', {
            'profile': profile,
        })
    
    context = {
        'profile': profile,
    }
    return render(request, 'projects/contact.html', context)
