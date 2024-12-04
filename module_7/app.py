from flask import Flask, render_template, request, redirect, url_for

import database

app = Flask('ONF Movies', static_folder='static')

@app.route("/")
def index():
    response = render_template('main.html', movies=database.movies())
    return response

@app.route('/movie/<int:id>')
def show_movie(id):
    response = render_template('movie.html',
                               movie=database.movie(id),
                               credits=database.credits(id))
    return response

@app.route('/new_movie')
def new_movie():
    no_credits = [{} for _ in range(10)]
    response = render_template('movie-form.html',
                               movie={},
                               credits=no_credits,
                               genres=database.genres())
    return  response

@app.route('/edit_movie/<int:id>')
def edit_movie(id):
    credits = database.credits(id)
    print(dict(database.movie(id)))
    padded_credits = credits + [{} for _ in range(10 - len(credits))]
    response = render_template('movie-form.html',
                               movie=database.movie(id),
                               credits=padded_credits,
                               genres=database.genres())
    return  response

@app.route('/save_movie', methods=['POST'])
def save_movie():
    print(request.form)
    movie = request.form
    id = movie['id']
    if id == '':
       id = database.add(movie)
    else:
        database.update(movie)
    return redirect(url_for('show_movie', id=id))