# ШПАРГАЛКА ШАБЛОН

def testSomething():
    something = makeSomething()
    assert  something.name is not None

import unittest

class TestAnyname(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a,b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a,b)

if __name__ == '__main__':
    unittest.main()

#----------

import unittest

class TestUnit1(unittest.TestCase):

    def test_is_x_greater_than_y(self):
        print('This is my first test')
        x = 8
        y = 6
        self.assertTrue(x > y, 'x > y')

    def test_isupper(self):
        print('This is my second test')
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())

if __name__ == '__main__':
    unittest.main()

#----------

import unittest

class TestStringMethod(unittest.TestCase):

    def test_upper(self):
        print('my test 1')
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.skip #если нужно пропустить кусок
    def test_split(self):
        print('my test 2')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

#----------

import unittest
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class TestMePlease(unittest.TestCase):

    def setUp(self) -> None:
        #service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Safari()#(service=service)
        self.driver.set_window_size(1024, 768)

    def test_1(self):
        self.driver.get('https://www.selenium.dev/about/')
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/documentation']").click()
        self.assertEqual(self.driver.title, 'About Selenium | Selenium')
        self.assertEqual(self.driver.current_url, "https://www.selenium.dev/documentation")
        time.sleep(3)

    def test_2(self):
        self.driver.get('https://www.selenium.dev/documentation')
        self.driver.execute_script("window.scrollTo(0,2500)")
        time.sleep(3)


    @unittest.skip('under development')
    def test_3(self):
        self.driver.get('https://www.getbootstrap.com')
        self.assertEqual(34, "")


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

#----------

import self as self
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest

class TestRocks(unittest.TestCase):
    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.set_window_size(1024,768)

    def test_rocks(self):
        self.driver.get('https://techstepacademy.com/trial-of-the-stones')

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

#----------

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRock(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Safari()
        self.driver.set_window_size(1024, 768)

    def test_1(self):
        self.driver.get('https://techstepacademy.com/trial-of-the-stones')
        time.sleep(3)
        input1 = self.driver.find_element(By.ID, "r1Input")
        button_answer = self.driver.find_element(By.ID, "r1Btn").click()
        button_bamboo = self.driver.find_element(By.CSS_SELECTOR, "#passwordBanner h4" )
        input1.send_keys('rock')

        # self.assertEqual(self.driver.title, 'About Selenium | Selenium')
        # self.assertEqual(self.driver.current_url, "https://www.selenium.dev/documentation")
        # time.sleep(3)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

#----------

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class TestWebsite(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Safari()
        self.driver.set_window_size(1024, 768)

    def test_open_website(self):
        self.driver.get('https://www.spletnik.ru')
        # time.sleep(3)
        # self.driver.find_element(By.XPATH,"//li[1]/a[2]")
        logo = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[1]/a")))

        self.assertTrue(logo.is_displayed())


    def tearDown(self) -> None:
            self.driver.close()

if __name__ == '__main__':
        unittest.main()

#----------


