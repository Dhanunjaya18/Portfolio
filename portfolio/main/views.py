from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, FileResponse, Http404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
import os

from .models import SiteProfile, Skill, Project, ContactMessage
from .forms import ContactForm


def get_site_profile():
    profile, _ = SiteProfile.objects.get_or_create(pk=1)
    return profile


def index(request):
    profile = get_site_profile()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    categories = list(Project.objects.values_list('category', flat=True).distinct())
    
    # Group skills by category
    skill_groups = {}
    for skill in skills:
        cat = skill.get_category_display()
        if cat not in skill_groups:
            skill_groups[cat] = []
        skill_groups[cat].append(skill)

    contact_form = ContactForm()
    
    context = {
        'profile': profile,
        'skills': skills,
        'skill_groups': skill_groups,
        'projects': projects,
        'categories': ['All'] + [c for c in categories if c and c != 'All'],
        'contact_form': contact_form,
    }
    return render(request, 'main/index.html', context)


def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = {field: list(errs) for field, errs in form.errors.items()}
                return JsonResponse({'success': False, 'errors': errors})
            messages.error(request, 'Please correct the errors below.')
            return redirect('index')
    return redirect('index')


def download_resume(request):
    profile = get_site_profile()
    if profile.resume_file:
        file_path = profile.resume_file.path
        if os.path.exists(file_path):
            response = FileResponse(open(file_path, 'rb'), as_attachment=True)
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    raise Http404("Resume not available.")


def projects_api(request):
    category = request.GET.get('category', 'All')
    projects = Project.objects.all()
    if category and category != 'All':
        projects = projects.filter(category=category)
    
    data = []
    for p in projects:
        data.append({
            'id': p.id,
            'title': p.title,
            'description': p.short_description or p.description[:150] + '...',
            'screenshot': p.screenshot.url if p.screenshot else '',
            'github_url': p.github_url,
            'live_url': p.live_url,
            'tags': p.get_tags_list(),
            'category': p.category,
            'featured': p.featured,
        })
    return JsonResponse({'projects': data})
