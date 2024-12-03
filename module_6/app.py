from jinja2 import Environment, FileSystemLoader, select_autoescape
from pprint import pp

import database

# ---- D A T A B A S E ----

movies = database.movies()
life_of_brian = database.movie(9)
credits = database.credits(life_of_brian['id'])
genres = database.genres()

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

render(template='main.html', outfile='main.html', movies=movies)

render(template='movie.html', outfile='movie.html', movie=life_of_brian, credits=credits)

no_credits = [{} for _ in range(10)]
render(template='movie-form.html', outfile='new-movie.html',
       title='New Movie', movie={}, credits=no_credits, genres=genres)

padded_credits = credits + [{} for _ in range(10 - len(credits))]
render(template='movie-form.html', outfile='edit-movie.html',
       title='Edit Movie', movie=life_of_brian, credits=padded_credits, genres=genres)
