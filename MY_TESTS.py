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

