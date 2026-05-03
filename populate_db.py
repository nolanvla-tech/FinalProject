#!/usr/bin/env python
"""
Script to populate the portfolio database with Nolan's projects, skills, and experiences.
Run with: python populate_db.py
"""
import os
import django
from datetime import date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_portfolio.settings')
django.setup()

from projects.models import Project, Skill, Experience

# Clear existing data (optional)
# Project.objects.all().delete()
# Skill.objects.all().delete()
# Experience.objects.all().delete()

print("=" * 60)
print("Populating Portfolio Database")
print("=" * 60)

# ==================== PROJECTS ====================
print("\nAdding Projects...")

projects_data = [
    {
        'title': 'Learning Log',
        'summary': 'A Django web application for tracking learning progress and notes',
        'business_problem': 'Need a simple way to document and organize learning materials across multiple topics',
        'description': 'A full-stack Django application that allows users to create topics and log entries. Features include user authentication, entry editing/deletion, and topic organization. Built with Django ORM, Bootstrap, and SQLite.',
        'category': 'django_app',
        'tools_used': 'Django, Python, SQLite, Bootstrap, HTML/CSS',
        'key_features': 'User authentication, Topic management, Entry logging and editing, Responsive design',
        'your_role': 'Full-stack developer - designed database schema, implemented all views and templates',
        'biggest_challenge': 'Implementing efficient database queries for large entry collections while maintaining performance',
        'lessons_learned': 'Importance of database indexing, user experience design, and clean code organization',
        'github_url': 'https://github.com/nolanvla-tech/learning-log',
        'is_featured': True,
        'display_order': 1,
    },
    {
        'title': 'Campus SkillSwap',
        'summary': 'A peer-to-peer skill sharing platform for college students',
        'business_problem': 'College students want to learn new skills from peers but lack a centralized platform to connect and coordinate',
        'description': 'A Django web application connecting students who want to teach and learn skills from each other. Features include skill profiles, matching algorithms, scheduling, and reviews. Designed to build community while facilitating knowledge transfer.',
        'category': 'django_app',
        'tools_used': 'Django, Python, PostgreSQL, Bootstrap, JavaScript, Django REST Framework',
        'key_features': 'Skill profiles and matching, User authentication, Scheduling system, Review and ratings, Notification system',
        'your_role': 'Led project architecture and backend development, implemented matching algorithm',
        'biggest_challenge': 'Building an intelligent matching algorithm that considers user preferences and availability',
        'lessons_learned': 'Importance of MVP approach, user testing, and scalable architecture design',
        'github_url': 'https://github.com/nolanvla-tech/campus-skillswap',
        'is_featured': True,
        'display_order': 2,
    },
    {
        'title': 'n8n Automation Workflow',
        'summary': 'Automated business process workflows using n8n no-code platform',
        'business_problem': 'Manual data entry and repetitive business processes were consuming significant time and prone to errors',
        'description': 'Designed and implemented comprehensive automation workflows using n8n connecting multiple APIs and services. Workflows handle data extraction, transformation, and integration across platforms including Slack, Gmail, Google Sheets, and custom databases.',
        'category': 'n8n_automation',
        'tools_used': 'n8n, APIs, Webhooks, Google Workspace, Slack, MongoDB',
        'key_features': 'Data extraction and transformation, Multi-platform integration, Error handling and logging, Scheduled execution',
        'your_role': 'Workflow architect and implementer - designed entire workflow logic and API integrations',
        'biggest_challenge': 'Handling complex error scenarios and ensuring reliability across multiple external services',
        'lessons_learned': 'Power of no-code platforms, importance of error handling, and API rate limit management',
        'github_url': 'https://github.com/nolanvla-tech/n8n-workflows',
        'is_featured': True,
        'display_order': 3,
    },
]

for project_data in projects_data:
    project, created = Project.objects.update_or_create(
        title=project_data['title'],
        defaults=project_data
    )
    status = "Created" if created else "Updated"
    print(f"  ✓ {status}: {project.title}")

# ==================== SKILLS ====================
print("\nAdding Skills...")

skills_data = [
    # Technical Skills
    ('Python', 'technical', 'expert'),
    ('Django', 'technical', 'advanced'),
    ('JavaScript', 'technical', 'intermediate'),
    ('SQL', 'technical', 'advanced'),
    ('HTML/CSS', 'technical', 'advanced'),
    ('Excel/VBA', 'technical', 'advanced'),
    ('Git/GitHub', 'technical', 'advanced'),
    ('APIs & Webhooks', 'technical', 'intermediate'),
    ('n8n', 'technical', 'intermediate'),
    ('PostgreSQL', 'technical', 'intermediate'),
    ('Bootstrap', 'technical', 'intermediate'),
    
    # Business Skills
    ('Financial Analysis', 'business', 'advanced'),
    ('Due Diligence', 'business', 'advanced'),
    ('Strategic Planning', 'business', 'advanced'),
    ('M&A Analysis', 'business', 'advanced'),
    ('Market Research', 'business', 'intermediate'),
    ('Business Modeling', 'business', 'intermediate'),
    ('Venture Analysis', 'business', 'intermediate'),
    
    # Soft Skills
    ('Leadership', 'soft', 'advanced'),
    ('Problem Solving', 'soft', 'expert'),
    ('Communication', 'soft', 'advanced'),
    ('Project Management', 'soft', 'advanced'),
    ('Team Collaboration', 'soft', 'advanced'),
    ('Critical Thinking', 'soft', 'advanced'),
    ('Adaptability', 'soft', 'advanced'),
    
    # Languages
    ('Spanish', 'language', 'intermediate'),
    ('English', 'language', 'expert'),
]

for i, (name, category, proficiency) in enumerate(skills_data, 1):
    skill, created = Skill.objects.update_or_create(
        name=name,
        defaults={
            'category': category,
            'proficiency': proficiency,
            'display_order': i
        }
    )
    status = "Created" if created else "Updated"
    print(f"  ✓ {status}: {skill.name} ({skill.get_category_display()})")

# ==================== EXPERIENCES ====================
print("\nAdding Experiences...")

experiences_data = [
    # Education
    {
        'title': 'Bachelor of Business Administration (BBA)',
        'company': 'Baylor University',
        'experience_type': 'education',
        'location': 'Waco, Texas',
        'start_date': date(2022, 8, 1),
        'end_date': date(2026, 5, 15),
        'description': 'Major: Finance, Strategy & MIS\nMinor: Entrepreneurship\nGPA: 3.82/4.0\nRelevant Coursework: Financial Analysis, Corporate Strategy, Business Analytics, Database Management',
    },
    # Work Experience
    {
        'title': 'Senior Analyst',
        'company': 'Baylor Angel Network',
        'experience_type': 'work',
        'location': 'Waco, Texas',
        'start_date': date(2024, 9, 1),
        'end_date': None,
        'description': 'Conduct early-stage venture analysis and due diligence\nEvaluate business models and financial projections\nAssist in investment decision-making processes\nManage portfolio company relationships',
    },
    {
        'title': 'Summer Financial Analyst',
        'company': 'Dell Technologies',
        'experience_type': 'work',
        'location': 'Austin, Texas',
        'start_date': date(2025, 6, 1),
        'end_date': date(2025, 8, 31),
        'description': 'Conducted financial analysis on business unit performance\nCreated executive dashboards and reporting systems\nAnalyzed quarterly revenue trends and forecasting\nSupported M&A due diligence process',
    },
    {
        'title': 'IT Implementations Intern',
        'company': 'Southwest Solutions Group',
        'experience_type': 'work',
        'location': 'Chicago, Illinois',
        'start_date': date(2024, 5, 1),
        'end_date': date(2024, 8, 31),
        'description': 'Implemented IT solutions for enterprise clients\nManaged project timelines and client communications\nTroubleshooting technical issues and supporting deployments\nDocumented processes and created user guides',
    },
    {
        'title': 'Revenue Cycle Management Intern',
        'company': 'Stella Mattina',
        'experience_type': 'work',
        'location': 'Chicago, Illinois',
        'start_date': date(2023, 6, 1),
        'end_date': date(2023, 8, 31),
        'description': 'Analyzed healthcare revenue cycles and billing processes\nIdentified cost reduction opportunities\nCreated process improvement recommendations\nTrained staff on new billing procedures',
    },
    # Leadership
    {
        'title': 'Board Member',
        'company': 'Bearly Used Sustainability Initiative',
        'experience_type': 'leadership',
        'location': 'Waco, Texas',
        'start_date': date(2023, 8, 1),
        'end_date': None,
        'description': 'Lead sustainability initiatives on campus\nCoordinate with administration on environmental policies\nOrganize community engagement and education events\nManage project budgets and timelines',
    },
    {
        'title': 'Leadership Consultant',
        'company': 'The Consulting Group (TCG) - Baylor',
        'experience_type': 'leadership',
        'location': 'Waco, Texas',
        'start_date': date(2024, 1, 1),
        'end_date': None,
        'description': 'Provide strategic consulting to student organizations\nFacilitate business planning and strategy sessions\nMentor emerging student leaders\nDevelop organizational best practices guides',
    },
]

for i, exp_data in enumerate(experiences_data, 1):
    exp, created = Experience.objects.update_or_create(
        title=exp_data['title'],
        company=exp_data['company'],
        start_date=exp_data['start_date'],
        defaults={
            'experience_type': exp_data['experience_type'],
            'location': exp_data['location'],
            'end_date': exp_data['end_date'],
            'description': exp_data['description'],
            'display_order': i,
        }
    )
    status = "Created" if created else "Updated"
    print(f"  ✓ {status}: {exp.title} at {exp.company}")

print("\n" + "=" * 60)
print("Database Population Complete!")
print("=" * 60)
