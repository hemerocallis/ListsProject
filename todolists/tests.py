from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from todolists.views import home_page

class HomePageTest(TestCase):
    '''unit tests for main page'''

    def test_uses_home_template(self):
        '''home page template test via Django test client'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
