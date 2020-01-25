from django.shortcuts import render

from .models import Project


def index(request):
    context = dict()
    context['projects'] = Project.objects.order_by('-start_date').values()
    return render(request, 'portfolio/index.html', context)
