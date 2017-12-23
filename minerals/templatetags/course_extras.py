from django import template

from minerals.models import Mineral

register = template.Library()


@register.inclusion_tag('group_nav.html')
def group_nav():
    """View displays list of minerals that matches search query by group"""
    groups = ['Silicates', 'Oxides', 'Sulfates', 'Sulfides', 'Carbonates',
              'Halides', 'Sulfosalts', 'Phosphates', 'Borates', 'Organic Minerals',
              'Arsenates', 'Native Elements', 'Other']
    return {'groups': groups}
