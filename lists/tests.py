from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')    #resolve is a django method for finding out what view a url string maps to
        self.assertEqual(found.func, home_page)     

    '''def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')

        #self.assertTrue(html.startswith('<html>'))
        #self.assertIn('<title>To-Do lists</title>', html)
        #self.assertTrue(html.strip().endswith('</html>'))

        self.assertEqual(html, expected_html)'''
    
    '''def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')'''
 
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text' : 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
    
'''class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)'''