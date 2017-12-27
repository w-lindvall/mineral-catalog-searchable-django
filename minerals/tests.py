from django.urls import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTest(TestCase):
    def test_mineral_model(self):
        """Test creation of mineral object"""
        mineral = Mineral.objects.create(
            name='A Test Mineral',
            category='Category',
            color='Color',
            crystal_system='Crystal System',
            luster='Luster',
            refractive_index='Refractive Index'
        )
        self.assertEqual(mineral.name, 'A Test Mineral')


class MineralViewTest(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='Amineral 1',
            category='Category 1',
            color='Color 1',
            group='Other',
        )
        self.mineral2 = Mineral.objects.create(
            name='Mineral 2',
            color='Color 2',
            streak='Streak 2',
            group='Rock'
        )

    def test_home_page_view(self):
        """Test home page view"""
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, self.mineral.name)
        # home page filters by first letter 'a'
        self.assertNotContains(response, self.mineral2.name)

    def test_detail_view(self):
        """Test detail view"""
        response = self.client.get(reverse('mineral_detail',
                                           kwargs={'pk': self.mineral.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mineral_detail.html')
        self.assertContains(response, self.mineral.name)
        self.assertContains(response, self.mineral.color)

    def test_mineral_name_search_view(self):
        """Test mineral name search view"""
        response = self.client.get(reverse('mineral_name_search'), {'q': 'Amineral'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.mineral.name)
        self.assertTemplateUsed(response, 'index.html')

    def test_mineral_group_search_view(self):
        """Test mineral group search view"""
        response = self.client.get(reverse('mineral_group_search', kwargs={'group': 'other'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.mineral.name)
        self.assertTemplateUsed(response, 'index.html')

    def test_mineral_first_search_view(self):
        """Test mineral first letter search view"""
        response = self.client.get(reverse('mineral_first_search', kwargs={'letter': 'a'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.mineral.name)
        self.assertTemplateUsed(response, 'index.html')
