from django.shortcuts import render
from .models import Profile, Project, Skill, Contact


def home(request):
    profile = Profile.objects.first()  # Only 1 profile assumed
    skills = Skill.objects.all()
    projects_preview = Project.objects.all()[:3]  # first 3 projects
    contact = Contact.objects.first()  # Only 1 contact assumed
    context = {
        'profile': profile,
        'skills': skills,
        'projects_preview': projects_preview,
        'contact': contact
    }
    return render(request, 'home.html', context)


def about(request):
    profile = Profile.objects.first()
    return render(request, 'about.html', {'profile': profile})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def contact(request):
    contact = Contact.objects.first()
    return render(request, 'contact.html', {'contact': contact})
