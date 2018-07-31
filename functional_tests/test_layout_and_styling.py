from .base import FunctionalTest
from .list_page import ListPage

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        list_page = ListPage(self)

        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = list_page.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # She starts a new list and sees the input is nicely
        # centered there too
        list_page.add_list_item('testing')

        inputbox = list_page.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )