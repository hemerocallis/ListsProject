from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
import time

class NewVisitorTest(LiveServerTestCase):
    '''new user test'''
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.CSS_SELECTOR, '#id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''user starts to-do list'''
        # user opens our main page
        self.browser.get(self.live_server_url)

        # user can see correct page title and header
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # user can see the offer to enter list item
        inputbox = self.browser.find_element(By.CSS_SELECTOR, '#id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # user can enter the first list item
        inputbox.send_keys('Learn TDD')

        # user can save list item: upon the page reload user can see
        # the previously entered list item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Learn TDD')

        # user still can see offer to enter list item
        inputbox = self.browser.find_element(By.CSS_SELECTOR, '#id_new_item')

        # user can create the second list item and see result list
        inputbox.send_keys('Create pet-project')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        self.check_for_row_in_list_table('1: Learn TDD')
        self.check_for_row_in_list_table('2: Create pet-project')

        # user can see text about unique URL address for the list

        # user can open their unique URL address of the created to-do list

        self.fail('End the test!')

if __name__ == '__main__':
    unittest.main()
