from django.shortcuts import render

from .models import Project, TechTag


def index(request):
    context = {
        'about_me': "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        'tab_id': 'about-tab'
    }

    return render(request, 'portfolio/index.html', context)


def projects(request, tag=None, proj_type="Personal"):
    context = {}
    if tag:
        try:
            context['projects'] = TechTag.objects.get(name=tag).projects.all()
            context['tag'] = tag
            context['tab_id'] = ''
        except TechTag.DoesNotExist:
            context['bad_tag'] = tag
            return render(request, 'portfolio/index.html', context={'bad_tag': tag})

    else:
        context['projects'] = Project.objects.order_by('-start_date').filter(type=proj_type)
        if proj_type == 'Personal':
            context['tab_id'] = 'pers-proj-tab'
        elif proj_type == 'OpenSource':
            context['tab_id'] = 'os-proj-tab'

    return render(request, 'portfolio/projects.html', context)


def detail(request, name):
    """Detailed information about projects"""
    try:
        context = {'project': Project.objects.get(name=name)}
    except Project.DoesNotExist:
        context = {'bad_name': name}
    return render(request, 'portfolio/detail.html', context)
