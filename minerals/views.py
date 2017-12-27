from django.shortcuts import render, get_object_or_404
import random

from .models import Mineral


def home_page(request):
    """View displays list of mineral names
    with links to individual detail view
    """
    groups = ['Silicates', 'Oxides', 'Sulfates', 'Sulfides', 'Carbonates',
              'Halides', 'Sulfosalts', 'Phosphates', 'Borates', 'Organic Minerals',
              'Arsenates', 'Native Elements', 'Other']
    all_minerals = Mineral.objects.all()
    random_mineral = random.choice(all_minerals)
    minerals = Mineral.objects.all().values('name', 'pk')
    return render(request, 'index.html', {'minerals': minerals, 'groups': groups, 'random': random_mineral})


def mineral_detail(request, pk):
    """View displays individual mineral details"""
    all_minerals = Mineral.objects.all()
    random_mineral = random.choice(all_minerals)
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'mineral_detail.html', {'mineral': mineral, 'random': random_mineral})


def mineral_name_search(request):
    """View displays list of minerals that matches search query by name"""
    term = request.GET.get('q')
    groups = ['Silicates', 'Oxides', 'Sulfates', 'Sulfides', 'Carbonates',
              'Halides', 'Sulfosalts', 'Phosphates', 'Borates', 'Organic Minerals',
              'Arsenates', 'Native Elements', 'Other']
    all_minerals = Mineral.objects.all()
    random_mineral = random.choice(all_minerals)
    minerals = Mineral.objects.filter(name__icontains=term).values('name',
                                                                   'pk')
    return render(request, 'index.html', {'minerals': minerals, 'groups': groups, 'random': random_mineral})


def mineral_group_search(request, group):
    """View displays list of minerals that matches search query by group"""
    groups = ['Silicates', 'Oxides', 'Sulfates', 'Sulfides', 'Carbonates',
              'Halides', 'Sulfosalts', 'Phosphates', 'Borates', 'Organic Minerals',
              'Arsenates', 'Native Elements', 'Other']
    all_minerals = Mineral.objects.all()
    random_mineral = random.choice(all_minerals)
    minerals = Mineral.objects.filter(group__contains=group).values('name', 'pk')
    return render(request, 'index.html', {'minerals': minerals, 'active_group': group, 'groups': groups, 'random': random_mineral})


def mineral_first_search(request, letter='a'):
    """View displays list of minerals that matches
    search query by first letter of name
    """
    groups = ['Silicates', 'Oxides', 'Sulfates', 'Sulfides', 'Carbonates',
              'Halides', 'Sulfosalts', 'Phosphates', 'Borates', 'Organic Minerals',
              'Arsenates', 'Native Elements', 'Other']
    all_minerals = Mineral.objects.all()
    random_mineral = random.choice(all_minerals)
    minerals = Mineral.objects.filter(name__istartswith=letter).values('name', 'pk')
    return render(request, 'index.html', {'minerals': minerals, 'active_letter': letter, 'groups': groups, 'random': random_mineral})
