from jinja2 import Environment, FileSystemLoader, select_autoescape
from pprint import pp

# ---- D A T A B A S E ----

movies = [
    {'id': 1, 'title': 'Shaun of the Dead',
     'year': 2004, 'rating': 6, 'genre': 'Comedy/Horror'},
    {'id': 2, 'title': 'Hot Fuzz',
     'year': 2007, 'rating': 6, 'genre': 'Action/Comedy'},
    {'id': 3, 'title': 'The World\'s End',
     'year': 2013, 'rating': 5, 'genre': 'Comedy/Sci-Fi'},
    {'id': 4, 'title': 'Blade Runner',
     'year': 1982, 'rating': 6, 'genre': 'Sci-Fi'},
    {'id': 5, 'title': 'Blade Runner 2049',
     'year': 2017, 'rating': 6, 'genre': 'Sci-Fi'},
    {'id': 6, 'title': 'The Princess Bride',
     'year': 1987, 'rating': 6, 'genre': 'Fantasy/Adventure'},
    {'id': 7, 'title': 'This Is Spinal Tap',
     'year': 1984, 'rating': 5, 'genre': 'Comedy/Mockumentary'},
    {'id': 8, 'title': 'Monty Python and the Holy Grail',
     'year': 1975, 'rating': 6, 'genre': 'Comedy'},
    {'id': 9, 'title': 'Monty Python\'s Life of Brian',
     'year': 1979, 'rating': 6, 'genre': 'Comedy'},
]

life_of_brian = movies[8]

credits = [
    {'name': 'Graham Chapman', 'role': 'Actor'},
    {'name': 'John Cleese',    'role': 'Actor'},
    {'name': 'Eric Idle',      'role': 'Actor'},
    {'name': 'Terry Gilliam',  'role': 'Actor'},
    {'name': 'Terry Jones',    'role': 'Actor'},
    {'name': 'Michael Palin',  'role': 'Actor'},
    {'name': 'Terry Jones',    'role': 'Director'},
    {'name': 'John Goldstone', 'role': 'Producer'},
]

genres = [
    'Action',
    'Action/Comedy',
    'Comedy',
    'Comedy/Horror',
    'Comedy/Mockumentary',
    'Comedy/Sci-Fi',
    'Drama',
    'Fantasy/Adventure',
    'Horror',
    'Romance',
    'Sci-Fi',
]

# ---- R E N D E R I N G ----

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

def render(template, outfile, **args):
    tmpl = env.get_template(template)
    print(f'Rendering {template} to {outfile}')
    if __debug__:
        pp(args)
        print('-----------')
    with open(outfile, 'w') as file:
        file.write(tmpl.render(**args))

sorted_movies = sorted(movies, key=lambda x: x['year'])
render(template='main.html', outfile='main.html', movies=sorted_movies)

render(template='movie.html', outfile='movie.html', movie=life_of_brian, credits=credits)

no_credits = [{} for _ in range(10)]
render(template='movie-form.html', outfile='new-movie.html',
       title='New Movie', movie={}, credits=no_credits, genres=genres)

padded_credits = credits + [{} for _ in range(10 - len(credits))]
render(template='movie-form.html', outfile='edit-movie.html',
       title='Edit Movie', movie=life_of_brian, credits=padded_credits, genres=genres)
