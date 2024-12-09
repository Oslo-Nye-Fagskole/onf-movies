import shared_setup
from bs4 import BeautifulSoup

import app as main_app

class AppTestCase(shared_setup.MovieTestCase):

    def setUp(self):
        super().setUp()

        app = main_app.app
        main_app.database = self.database
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.app.testing = True

    def test_main(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Shaun of the Dead", response.text)

    def test_navigate_to_movie_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Shaun of the Dead", response.text)

        soup = BeautifulSoup(response.data, 'html.parser')
        link = soup.find('a', string="Shaun of the Dead")['href']
        next_response = self.app.get(link)
        
        self.assertEqual(next_response.status_code, 200)
        self.assertIn('<h2>Shaun of the Dead</h2>', next_response.text)
        self.assertIn('credits', next_response.text)

    def test_new_movie(self):
        response = self.app.get('/movie/new')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.data, 'html.parser')
        url = soup.find('form')['action']
        save_response = self.app.post(url, data={
            'id': '',
            'title': 'Test Movie',
            'genre': 'Comedy',
            'release_year': 2024,
            'rating': 2,
            'credits[name]': 'Test Name',
            'credits[role]': 'Test Role',
        }, follow_redirects=True)
        self.assertEqual(len(save_response.history), 1)
        self.assertEqual(save_response.request.path, "/movie/10")
        self.assertEqual(save_response.status_code, 200)

    def test_edit_movie(self):
        response = self.app.get('/movie/1/edit')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.data, 'html.parser')
        url = soup.find('form')['action']
        save_response = self.app.post('/movie/save', data={
            'id': '1',
            'title': 'Test Movie',
            'genre': 'Comedy',
            'release_year': 2024,
            'rating': 2,
            'credits[name]': 'Test Name',
            'credits[role]': 'Test Role',
        }, follow_redirects=True)
        self.assertEqual(len(save_response.history), 1)
        self.assertEqual(save_response.request.path, "/movie/1")
        self.assertEqual(save_response.status_code, 200)
    

        