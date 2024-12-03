from jinja2 import Environment, FileSystemLoader, select_autoescape
from pprint import pp

import database

life_of_brian_id = 9

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

render(template='main.html', outfile='main.html', movies=database.movies())

render(template='movie.html', outfile='movie.html',
        movie=database.movie(life_of_brian_id), credits=database.credits(life_of_brian_id))

no_credits = [{} for _ in range(10)]
render(template='movie-form.html', outfile='new-movie.html',
       title='New Movie', movie={}, credits=no_credits, genres=database.genres())

credits = database.credits(life_of_brian_id)
padded_credits = credits + [{} for _ in range(10 - len(credits))]
render(template='movie-form.html', outfile='edit-movie.html',
       title='Edit Movie', movie=database.movie(life_of_brian_id), credits=padded_credits, genres=database.genres())
