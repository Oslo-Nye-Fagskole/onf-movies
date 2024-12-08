import unittest
from bs4 import BeautifulSoup

from database import MovieDatabase
import app as main_app

class DatabaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.database = MovieDatabase(':memory:')
        with open("movie_database_dump.sql", "r") as file:
            sql_script = file.read()
        cursor = cls.database.cursor()
        cursor.executescript(sql_script)

    def setUp(self):
        self.database = self.__class__.database
        self.database.cursor().execute('BEGIN TRANSACTION')

         # Initialize Flask test client
        app = main_app.app
        main_app.db = self.database
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        self.database.cursor().execute('ROLLBACK')

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
        save_response = self.app.post('/movie/save', data={
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


   