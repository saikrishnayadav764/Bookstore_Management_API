import unittest
from flask import Flask
from app import create_app


class TestRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = create_app()
        app.config['TESTING'] = True
        cls.app = app.test_client()
        cls.base_url = '/api'  
        cls.access_token = cls.get_access_token()

    @classmethod
    def get_access_token(cls):
        response = cls.app.post(
            f'{cls.base_url}/login',
            json={'username': 'admin', 'password': 'admin'}
        )
        data = response.json
        return data['access_token']

    def test_add_book(self):
        response = self.app.post(
            f'{self.base_url}/books',
            json={
                'title': 'Test Book',
                'author': 'Test Author',
                'ISBN': '1234567890',
                'publication_date': '2022-01-01'
            },
            headers={'Authorization': f'Bearer {self.access_token}'}
        )
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        response = self.app.get(
            f'{self.base_url}/books',
            headers={'Authorization': f'Bearer {self.access_token}'}
        )
        self.assertEqual(response.status_code, 200)

    def test_get_book(self):
        response = self.app.get(
            f'{self.base_url}/books/1234567890',
            headers={'Authorization': f'Bearer {self.access_token}'}
        )
        self.assertEqual(response.status_code, 200)  

    def test_update_book(self):
        response = self.app.put(
            f'{self.base_url}/books/1234567890',
            json={
                'title': 'Updated Test Book',
                'author': 'Updated Test Author',
                'publication_date': '2023-01-01'
            },
            headers={'Authorization': f'Bearer {self.access_token}'}
        )
        self.assertEqual(response.status_code, 200) 

    def test_delete_book(self):
        response = self.app.delete(
            f'{self.base_url}/books/1234567890',
            headers={'Authorization': f'Bearer {self.access_token}'}
        )
        self.assertEqual(response.status_code, 200)  


if __name__ == '__main__':
    unittest.main()
