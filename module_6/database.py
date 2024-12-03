import sqlite3
from pprint import pp

con = sqlite3.connect("movie_database.db")
con.row_factory = sqlite3.Row
cur = con.cursor()

def movies():
    cur.execute(f'SELECT * FROM movies ORDER BY release_year')
    return cur.fetchall()

def movie(id):
    cur.execute(f'SELECT * FROM movies WHERE id = ?', (id,))
    return cur.fetchone()

def credits(movie_id):
    cur.execute(f'SELECT * FROM credits WHERE movie_id = ?', (movie_id,))
    return cur.fetchall()

def genres():
    cur.execute(f'SELECT * FROM genres')
    return [row[0] for row in cur.fetchall()]

def ppr(rows):
    pp([dict(r) for r in rows])

def main():
    print("# ONF MOVIES")    
    print("## ALL MOVIES")
    ppr(movies())
    print("## MOVIE #1")
    pp(dict(movie(1)))
    print("### CREDITS")
    ppr(credits(1))

if __name__ == '__main__':
    main()