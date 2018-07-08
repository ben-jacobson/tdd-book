from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time, os 

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):                   # inherits from unittest.TestCase which lays out the framework for unit testing
    def setUp(self):
        self.browser = webdriver.Firefox()
        #time.sleep(1)                                            # sometimes encountering a bug wher making changes to the web driver too soon causes a pipe error
        self.browser.set_page_load_timeout(30)

        staging_server = os.environ.get('STAGING_SERVER')           # relies on a one-time setting of environment variables. Without using "export VAR_NAME", the variable will reset immediately after exection

        if staging_server:
            self.live_server_url = 'http://' + staging_server    

    def tearDown(self):                                     # setup and tearDown are inherited from unittest.TestCase and overwritten to perform specific functions that we control
        self.browser.quit()

    # helper function, refactoring a piece of code that is re-used 3 times in these tests
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try: 
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows]) 
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5) 