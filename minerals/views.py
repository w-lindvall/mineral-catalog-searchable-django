from django.shortcuts import render, get_object_or_404

from .models import Mineral


def home_page(request):
    """View displays list of mineral names
    with links to individual detail view
    """
    minerals = Mineral.objects.all()
    return render(request, 'index.html', {'minerals': minerals})


def mineral_detail(request, pk):
    """View displays individual mineral details"""
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'mineral_detail.html', {'mineral': mineral})
