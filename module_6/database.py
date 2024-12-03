import sqlite3
from pprint import pp

con = sqlite3.connect("movie_database.db")
con.row_factory = sqlite3.Row

def movies():
    cur = con.cursor()
    cur.execute(f'SELECT * FROM movies ORDER BY release_year')
    return cur.fetchall()

def movie(id):
    cur = con.cursor()
    cur.execute(f'SELECT * FROM movies WHERE id = ?', (id,))
    return cur.fetchone()

def credits(movie_id):
    cur = con.cursor()
    cur.execute(f'SELECT * FROM credits WHERE movie_id = ?', (movie_id,))
    return cur.fetchall()

def genres():
    cur = con.cursor()
    cur.execute(f'SELECT * FROM genres')
    return [row[0] for row in cur.fetchall()]


def main():
    print("# ONF MOVIES")    
    print("## ALL MOVIES")
    rows = movies()
    pp([dict(r) for r in rows])
    print("## MOVIE #1")
    rows = movie(1)
    pp([dict(r) for r in rows])
    print("### CREDITS")
    rows = credits(1)
    pp([dict(r) for r in rows])

if __name__ == '__main__':
    main()