from selenium import webdriver
from time import sleep
import unittest

class NewVistitorTest(unittest.TestCase):                   # inherits from unittest.TestCase which lays out the framework for unit testing
    def setUp(self):
        self.browser = webdriver.Firefox()
        sleep(1)                                            # encountering a bug wher making changes to the web driver too soon causes a pipe error
        self.browser.set_page_load_timeout(30)

    def tearDown(self):                                     # setup and tearDown are inherited from unittest.TestCase and overwritten to perform specific functions that we control
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  # any method within the test case class is considered a test, and is automatically run
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        #assert 'To-Do' in browser.title, "Browser Title was '" + browser.title + "'"
        self.assertIn('To-Do', self.browser.title)          # assertIn equivalent of 'if x in y' or assert 'x' in y:
        self.fail('Finish the test!')                       # at the moment just a reminder to finish the test

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)

        # The page updates again, and now shows both items on her list

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')