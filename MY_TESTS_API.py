import unittest
import requests

TARGET_API = 'https://www.breakingbadapi.com/api/'
HTTP_OK = 200
TOTAL_CHARACTERS = 62

class TestMyApi(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_fetch_all_characters(self):
        response = requests.get(f'{TARGET_API}characters')
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertEqual(len(response.json()), TOTAL_CHARACTERS, f'Failed: expected fetch data about {TOTAL_CHARACTERS} characters!')

    def test_fetch_first_character(self):
        response = requests.get(f'{TARGET_API}characters/1')
        self.assertEqual(response.status_code, HTTP_OK)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['char_id'], 1)
        self.assertEqual(data[0]['name'], 'Walter White')

    def test_fetch_all_quotes_from_the_series(self):
        response = requests.get(f'{TARGET_API}quotes?series=Better+Call+Saul')
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertEqual(len(response.json()), 18, 'Failed')

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()



#----------


import unittest
import requests

TARGET_API = 'https://jsonplaceholder.typicode.com'
HTTP_OK =200
TOTAL_POSTS = 4
TOTAL_POSTS_1 = 100

class TestJsonAPI(unittest.TestCase):

    def setUp(self) -> None:
        pass
    # @unittest.skip
    def test_get_post_1(self):
        response = requests.get(f'{TARGET_API}/posts/1')
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertEqual(len(response.json()), TOTAL_POSTS, f'failed not {TOTAL_POSTS}')

    @unittest.skip
    def test_get_post_2(self):
        response = requests.get(f'{TARGET_API}/posts')
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertEqual(len(response.json()), TOTAL_POSTS_1, f'failed not {TOTAL_POSTS_1}')

    @unittest.skip
    def test_get_post_3(self):
        response = requests.get(f'{TARGET_API}/posts/1')
        data = response.json()
        self.assertEqual(response.status_code, HTTP_OK)
        actual_keys = list(data.keys())
        expected_keys = ['userId', 'id', 'title', 'body']
        for i in range(len(expected_keys)):
            self.assertEqual(actual_keys[i], expected_keys[i])

    @unittest.skip
    def test_post_post(self):
        payload = {
            'title': 'ogogo',
            'body': 'bar',
            'user Id': 1,
        }
        response = requests.post(f'{TARGET_API}/posts', payload)
        data = response.json()

        expected_title = 'ogogo'
        actual_title = data['title']

        self.assertEqual(actual_title, expected_title, 'error-error-error')

    @unittest.skip
    def test_put_post(self):
        payload = {
            'body': 'new_body',
        }
        response = requests.put(f'{TARGET_API}/posts/1', payload)
        # response = requests.get(f'{TARGET_API}/posts/1')
        data = response.json()
        print(data)

    def test_delete(self):
        response = requests.delete(f'{TARGET_API}/posts/1')
        data = response.json()
        print(data)



    def tearDown(self) -> None:
            pass

if __name__ == '__main__':
        unittest.main()


#----------

