import unittest
from selenium import webdriver
from ddt import ddt, data, unpack
from utilities.test_data_loader import get_csv_data
import time

@ddt
class ISphereTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://www.google.com")

    @data(*get_csv_data("..\\data\\test_data.csv"))
    @unpack
    def test_search_keyword(self, search_value, expected_link):
        self.search_in_google(search_value)
        self.verify_search_result_link(expected_link)

    def search_in_google(self, search_value):
        driver = self.driver
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys(search_value)
        driver.find_element_by_name("btnG").click()
        time.sleep(2)

    def verify_search_result_link(self, expected_link):
        driver = self.driver
        actual_link_value = driver.find_element_by_xpath(".//div[@id='rso']/descendant::h3[@class ='r']/a").get_attribute("href")
        self.assertEqual(expected_link, actual_link_value)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
