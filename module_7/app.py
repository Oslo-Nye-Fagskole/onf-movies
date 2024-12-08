from flask import Flask, g, render_template, request, redirect, url_for

from database import MovieDatabase

app = Flask('ONF Movies', static_folder='static')
db = MovieDatabase()

@app.before_request
def load_db():
    g.db = db

@app.route("/")
def index():
    response = render_template('main.html', movies=g.db.movies())
    return response

@app.route('/movie/<int:id>')
def show_movie(id):
    response = render_template('movie.html',
                               movie=g.db.movie(id),
                               credits=g.db.credits(id))
    return response

@app.route('/movie/new')
def new_movie():
    no_credits = [{} for _ in range(10)]
    response = render_template('movie-form.html',
                               movie={},
                               credits=no_credits,
                               genres=g.db .genres())
    return  response

@app.route('/movie/<int:id>/edit')
def edit_movie(id):
    credits = g.db .credits(id)
    padded_credits = credits + [{} for _ in range(10 - len(credits))]
    response = render_template('movie-form.html',
                               movie=g.db .movie(id),
                               credits=padded_credits,
                               genres=g.db .genres())
    return  response

@app.route('/movie/save', methods=['POST'])
def save_movie():
    movie = request.form
    id = movie['id']
    if id == '':
       id = g.db .add(movie)
    else:
        g.db .update(movie)
    _set_credits(g, int(id), movie)
    return redirect(url_for('show_movie', id=id))

def _set_credits(g, id, form):
    names = list(filter(None, form.getlist('credits[name]')))
    roles = list(filter(None, form.getlist('credits[role]')))
    ids = [id] * len(names)
    credits = list(zip(ids, names, roles))
    g.db.set_credits(id, credits)
