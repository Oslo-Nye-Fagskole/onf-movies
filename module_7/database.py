import sqlite3

class MovieDatabase:

    def __init__(self, database='movie_database.db'):
        self.database = database
        con = sqlite3.connect(database, autocommit=True)
        con.row_factory = sqlite3.Row
        if __debug__:
            con.set_trace_callback(lambda query: print(f'Executed SQL: {query}'))
        self.connection = con

    def cursor(self):
        return self.connection.cursor()

    def movies(self):
        cur = self.cursor()
        cur.execute('SELECT * FROM movies ORDER BY release_year')
        return cur.fetchall()

    def movie(self, movie_id):
        cur = self.cursor()
        cur.execute('SELECT * FROM movies WHERE id = ?', (movie_id,))
        return cur.fetchone()

    def credits(self, movie_id):
        cur = self.cursor()
        cur.execute('SELECT * FROM credits WHERE movie_id = ?', (movie_id,))
        return cur.fetchall()

    def genres(self):
        cur = self.cursor()
        cur.execute('SELECT * FROM genres')
        return [r['name'] for r in cur.fetchall()]

    def update(self, movie):
        cur = self.cursor()
        cur.execute('UPDATE movies set title = ?, release_year = ?, genre = ?, rating = ? WHERE id = ?', 
                    (movie['title'], int(movie['release_year']), movie['genre'], 
                    int(movie['rating']), int(movie['id'])))

    def add(self, movie):
        cur = self.cursor()
        cur.execute('INSERT INTO movies (title, release_year, genre, rating) VALUES (?,?,?,?)',
                    (movie['title'], int(movie['release_year']), movie['genre'], int(movie['rating'])))
        id = cur.lastrowid
        return id

    def set_credits(self, id, credits):
        cur = self.cursor()
        cur.execute('DELETE FROM credits WHERE movie_id = ?', (id,))
        cur.executemany('INSERT INTO credits (movie_id, name, role) VALUES (?, ?, ?)', credits)

