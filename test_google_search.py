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
        
    def test_search_redirect(self):
        driver = self.driver
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium WebDriver")
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)  
        self.assertIn("search", driver.current_url)
        
    def test_results_page_elements(self):
        driver = self.driver
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Automation testing with Selenium")
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)  

        self.assertTrue(driver.find_element(By.NAME, "q"))

        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        self.assertGreater(len(results), 0, "No se encontraron resultados de búsqueda.")

    def test_number_of_results(self):
        driver = self.driver
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Python programming")
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)  

        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        self.assertGreater(len(results), 0, "No se encontraron resultados de búsqueda.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
