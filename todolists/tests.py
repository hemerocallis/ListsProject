from django.test import TestCase

class SmokeTest(TestCase):
    '''smoke unit tests'''

    def test_bad_maths(self):
        '''sample test'''
        self.assertEqual(2 * 2, 5)
