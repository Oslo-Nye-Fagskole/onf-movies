import unittest

from database import MovieDatabase

class MovieTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.database = MovieDatabase(':memory:')
        with open("movie_database_dump.sql", "r") as file:
            sql_script = file.read()
        cursor = cls.database.cursor()
        cursor.executescript(sql_script)

    @classmethod
    def tearDownClass(cls):
        cls.database.close()

    def setUp(self):
        self.database = self.__class__.database
        self.database.cursor().execute('BEGIN TRANSACTION')

    def tearDown(self):
        self.database.cursor().execute('ROLLBACK')

