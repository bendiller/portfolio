from django.shortcuts import render

from .models import Project


def index(request):
    """Provide Projects as list of 2-tuples for easier 2-column display by template"""
    proj_list = Project.objects.order_by('-start_date')
    tup_list = list()
    for i, _ in enumerate(proj_list[::2]):
        try:
            tup_list.append((proj_list[2*i], proj_list[2*i + 1]))
        except IndexError:  # Deals with final iteration when len(proj_list) is odd.
            tup_list.append((proj_list[2*i], False))

    context = {'projects': tup_list}
    return render(request, 'portfolio/index.html', context)
