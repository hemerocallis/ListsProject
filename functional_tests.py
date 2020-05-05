from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

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

        table = self.browser.find_element(By.CSS_SELECTOR, '#id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(any(row.text == '1: Learn TDD' for row in rows),\
        "New item is not shown in the table")

        # user still can see offer to enter list item

        # user can create the second list item and see result list

        # user can see text about unique URL address for the list

        # user can open their unique URL address of the created to-do list

        self.fail('End the test!')

if __name__ == '__main__':
    unittest.main()
