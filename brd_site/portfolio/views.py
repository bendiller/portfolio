from django.shortcuts import render

from .models import Project, TechTag


def index(request, tag=None):
    """Provide Projects as list of 2-tuples for easier 2-column display by template"""
    context = {}
    if tag:
        try:
            proj_list = TechTag.objects.get(name=tag).projects.all()
            context['tag'] = tag
        except TechTag.DoesNotExist:
            context['bad_tag'] = tag
            return render(request, 'portfolio/index.html', context={'bad_tag': tag})

    else:
        proj_list = Project.objects.order_by('-start_date')
    tup_list = list()
    for i, _ in enumerate(proj_list[::2]):
        try:
            tup_list.append((proj_list[2*i], proj_list[2*i + 1]))
        except IndexError:  # Deals with final iteration when len(proj_list) is odd.
            tup_list.append((proj_list[2*i], False))

    context['projects'] = tup_list
    return render(request, 'portfolio/index.html', context)


def detail(request, name):
    """Detailed information about projects"""
    try:
        context = {'project': Project.objects.get(name=name)}
    except Project.DoesNotExist:
        context = {'bad_name': name}
    return render(request, 'portfolio/detail.html', context)
