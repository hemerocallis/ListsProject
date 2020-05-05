from django.test import TestCase
from django.urls import resolve
from todolists.views import home_page

class HomePageTest(TestCase):
    '''unit tests for main page'''

    def test_root_url_resolves_to_home_page_view(self):
        '''sample test'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

