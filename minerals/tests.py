from django.urls import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTest(TestCase):
    def test_mineral_model(self):
        """Test creation of mineral object"""
        mineral = Mineral.objects.create(
            name='Test Mineral',
            category='Category',
            color='Color',
            crystal_system='Crystal System',
            luster='Luster',
            refractive_index='Refractive Index'
        )
        self.assertEqual(mineral.name, 'Test Mineral')


class MineralViewTest(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='Mineral 1',
            category='Category 1',
            color='Color 1',
        )
        self.mineral2 = Mineral.objects.create(
            name='Mineral 2',
            color='Color 2',
            streak='Streak 2',
        )

    def test_home_page_view(self):
        """Test home page view"""
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.mineral, response.context['minerals'])
        self.assertIn(self.mineral2, response.context['minerals'])
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn(self.mineral, response.context['minerals'])
        self.assertIn(self.mineral2, response.context['minerals'])

    def test_detail_view(self):
        """Test detail view"""
        response = self.client.get(reverse('mineral_detail',
                                           kwargs={'pk': self.mineral.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mineral_detail.html')
        self.assertContains(response, self.mineral.name)
        self.assertContains(response, self.mineral.color)
