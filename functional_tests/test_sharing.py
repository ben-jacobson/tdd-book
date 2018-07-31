from .base import FunctionalTest
from .list_page import ListPage
from .my_lists_page import MyListsPage

def quit_if_possible(browser):
    #try: browser.quit()
    #except: pass
    browser.quit()

class SharingTest(FunctionalTest):
    def test_can_share_a_list_with_another_user_pt1(self):
        list_page = ListPage(self)
        
        # Edith is a logged-in user
        self.create_pre_authenticated_session('edith@example.com')

        # Edith goes to the home page and starts a list
        self.browser.get(self.live_server_url)
    
        list_page.add_list_item('Get help')
        
        # She notices a "Share this list" option
        share_box = list_page.get_share_box()
        
        # and notices that the placeholder "your-friend@example.com" is present
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )
        
        # She shares her list by entering the email address of a friend
        # The page updates to say that it's shared with Oniciferous:
        list_page.share_list_with('oniciferous@example.com')


    # NOTE - in order for this to work, all 3 parts need to be made part of the same test. Because otherwise, the temporary database used is destroyed between tests, creating a false error
    def test_can_share_a_list_with_another_user_pt2(self):
        list_page = ListPage(self)

        # Ediths friend Oniciferous is also hanging out on the lists site as a logged in user
        self.create_pre_authenticated_session('oniciferous@example.com')

        # Oniciferous goes to the lists page with his browser
        MyListsPage(self).go_to_my_lists_page()

        # He sees Edith's list in there!
        self.browser.find_element_by_link_text('Get help').click()

        # On the list page, Oniciferous can see says that it's Edith's list
        self.wait_for(lambda: self.assertEqual(
            list_page.get_list_owner(),
            'edith@example.com'
        ))

        # He adds an item to the list
        list_page.add_list_item('Hi Edith!')

    def test_can_share_a_list_with_another_user_pt3(self):
        list_page = ListPage(self)

        # When Edith refreshes the page, she sees Oniciferous's addition
        self.create_pre_authenticated_session('edith@example.com')

        # Edith goes to the lists page in her browser
        MyListsPage(self).go_to_my_lists_page()

        # She clicks on the list that she created earlier
        self.browser.find_element_by_link_text('Get help').click()

        # And finds that Oniciferous has added something to her list
        list_page.wait_for_row_in_list_table('Hi Edith!', 2)
        
    
        