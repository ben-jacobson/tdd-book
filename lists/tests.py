from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')    #resolve is a django method for finding out what view a url string maps to
        self.assertEqual(found.func, home_page)     

'''class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)'''