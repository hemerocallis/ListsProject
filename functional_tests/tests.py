from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import unittest
import time
import os

MAX_WAIT = 10

class NewVisitorTest(StaticLiveServerTestCase):
    '''new user test'''
    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.CSS_SELECTOR, '#id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def test_layout_and_styling(self):
        '''styles check'''
        # user opens home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # user can see centered input field
        inputbox = self.browser.find_element(By.CSS_SELECTOR, '#id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10)

        # user can start a new list and see centered input field on list page
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element(By.CSS_SELECTOR, '#id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10)


    def test_can_start_a_list_for_one_user(self):
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

        self.wait_for_row_in_list_table('1: Learn TDD')

        # user still can see offer to enter list item
        inputbox = self.browser.find_element(By.CSS_SELECTOR, '#id_new_item')

        # user can create the second list item and see result list
        inputbox.send_keys('Create pet-project')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Learn TDD')
        self.wait_for_row_in_list_table('2: Create pet-project')

        # user can see text about unique URL address for the list

        # user can open their unique URL address of the created to-do list

        self.fail('End the test!')


    def test_multiple_users_can_start_lists_at_different_urls(self):
        '''multiple users test'''
        # user1 starts a new list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.CSS_SELECTOR, '#id_new_item')
        inputbox.send_keys('Learn TDD')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Learn TDD')

        # user1 can see unique url of the created list
        user1_list_url = self.browser.current_url
        self.assertRegex(user1_list_url, '/lists/.+')

        self.browser.quit()
        self.browser = webdriver.Firefox()

        # user2 opens home page and don't see user1's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Learn TDD', page_text)
        self.assertNotIn('Create pet-project', page_text)

        # user2 starts a new list
        inputbox = self.browser.find_element(By.CSS_SELECTOR, '#id_new_item')
        inputbox.send_keys('Automate testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Automate testing')

        # user2 takes own unique url
        user2_list_url = self.browser.current_url
        self.assertRegex(user2_list_url, '/lists/.+')
        self.assertNotEqual(user2_list_url, user1_list_url)

        # user2 don't see user1's list
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Learn TDD', page_text)
        self.assertIn('Automate testing', page_text)


if __name__ == '__main__':
    unittest.main()
