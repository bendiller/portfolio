from django.shortcuts import render

from .models import Project, TechTag


def index(request, tag=None):
    context = {}
    if tag:
        try:
            context['projects'] = TechTag.objects.get(name=tag).projects.all()
            context['tag'] = tag
        except TechTag.DoesNotExist:
            context['bad_tag'] = tag
            return render(request, 'portfolio/index.html', context={'bad_tag': tag})

    else:
        context['projects'] = Project.objects.order_by('-start_date')

    return render(request, 'portfolio/index.html', context)


def detail(request, name):
    """Detailed information about projects"""
    try:
        context = {'project': Project.objects.get(name=name)}
    except Project.DoesNotExist:
        context = {'bad_name': name}
    return render(request, 'portfolio/detail.html', context)
