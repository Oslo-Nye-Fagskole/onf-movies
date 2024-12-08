import unittest

from database import MovieDatabase

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

    def tearDown(self):
        self.database.cursor().execute('ROLLBACK')

    def test_movies(self):
        movies = self.database.movies()
        self.assertEqual(len(movies), 9)
        expected = {'id': 8, 
                    'title': 'Monty Python and the Holy Grail',
                    'genre': 'Comedy',
                    'release_year': 1975,
                    'rating': 6}
        self.assertEqual(dict(movies[0]), expected)

    def test_movie(self):
        movie = self.database.movie(1)
        expected = {'id': 1, 
                    'title': 'Shaun of the Dead',
                    'genre': 'Comedy/Horror',
                    'release_year': 2004,
                    'rating': 6}
        self.assertEqual(dict(movie), expected)

    def test_credits(self):
        credits = self.database.credits(1)
        self.assertEqual(len(credits), 5)
        expected = {'movie_id': 1, 'name': 'Edgar Wright', 'role': 'Director'}
        self.assertEqual(dict(credits[0]), expected)

    def test_add(self):
        movie = {'title': 'Test Movie',
                 'genre': 'Comedy',
                 'release_year': 2024,
                 'rating': 2 }
        id = self.database.add(movie)
        self.assertEqual(id, 10)

    def test_update(self):
        movie1 = dict(self.database.movie(1))
        movie1['rating'] = 1
        self.database.update(movie1)
        movie2 = dict(self.database.movie(1))
        self.assertEqual(movie2, movie1)

    def set_credits(self):
        new_credits = [(1, 'Test Person', 'Test Role')]
        self.database.set_credits(1, new_credits)
        self.assertEqual(len(self.database.credits(1)), 1)


