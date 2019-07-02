from selenium import webdriver
import unittest
class Baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.baidu.com")
    def test_01(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
    @classmethod
    def tearDownClass(cls):
        
        
        pass
if __name__ == '__main__':
       unittest.main(verbosity=2)



