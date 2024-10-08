import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_google_search(self):
        driver = self.driver
        driver.get("https://www.google.com")

        time.sleep(2)

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Automation testing with Selenium in Safari")
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)
        self.assertIn("Automation testing with Selenium", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
