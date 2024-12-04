import sqlite3
from pprint import pp

def cursor():
    con = sqlite3.connect("movie_database.db", autocommit=True)
    con.row_factory = sqlite3.Row
    con.set_trace_callback(lambda query: print(f'Executed SQL: {query}'))
    return con.cursor()

def movies():
    cur = cursor()
    cur.execute('SELECT * FROM movies ORDER BY release_year')
    return cur.fetchall()

def movie(movie_id):
    cur = cursor()
    cur.execute('SELECT * FROM movies WHERE id = ?', (movie_id,))
    return cur.fetchone()

def credits(movie_id):
    cur = cursor()
    cur.execute('SELECT * FROM credits WHERE movie_id = ?', (movie_id,))
    return cur.fetchall()

def genres():
    cur = cursor()
    cur.execute('SELECT * FROM genres')
    return [r['name'] for r in cur.fetchall()]

def update(movie):
    cur = cursor()
    cur.execute('UPDATE movies set title = ?, release_year = ?, genre = ?, rating = ? WHERE id = ?', 
                (movie['title'], int(movie['release_year']), movie['genre'], 
                 int(movie['rating']), int(movie['id'])))
    names = list(filter(None, movie.getlist('participants[name]')))
    roles = list(filter(None, movie.getlist('participants[role]')))
    ids = [int(movie['id']) for _ in range(len(names))]
    credits = list(zip(ids, names, roles))
    cur.execute('DELETE FROM credits WHERE movie_id = ?', (movie['id'],))
    cur.executemany('INSERT INTO credits (movie_id, name, role) VALUES (?, ?, ?)', credits)

def test():
    pp([dict(r) for r in movies()])
    print('-------------------------------')
    pp(dict(movie(1)))
    print('-------------------------------')
    pp([dict(r) for r in credits(1)])
    print('-------------------------------')
    pp(genres())

if __name__ == '__main__':
    test()