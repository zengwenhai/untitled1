import unittest
from selenium import webdriver

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_baidu_new(self):
        self.driver.find_element_by_link_text("新闻").click()
        self.assertEqual(self.driver.current_url, 'http://news.baidu.com/')


if __name__ == "__main__":
    unittest.main(verbosity=2)