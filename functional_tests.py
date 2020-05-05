from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    '''new user test'''
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''user starts to-do list'''
        # user opens our main page
        self.browser.get('http://localhost:8000')

        # user can see correct page title
        assert 'To-Do' in self.browser.title,\
        "Something went wrong :("

        # user can see the offer to enter list item

        # user can enter the first list item

        # user can save list item: upon the page reload user can see
        # the previously entered list item

        # user still can see offer to enter list item

        # user can create the second list item and see result list

        # user can see text about unique URL address for the list

        # user can open their unique URL address of the created to-do list

if __name__ == '__main__':
    unittest.main()
