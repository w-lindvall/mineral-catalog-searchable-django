from django.shortcuts import render

from .models import Mineral


def home_page(request):
    """View displays list of mineral names with links"""
    minerals = Mineral.objects.all()
    return render(request, 'index.html', {'minerals': minerals})
