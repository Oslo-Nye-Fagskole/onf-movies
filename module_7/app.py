from flask import Flask, render_template

import database

app = Flask('ONF Movies', static_folder='static')

@app.route("/")
def index():
    response = render_template('main.html', movies=database.movies())
    return response

@app.route('/movie/<int:id>')
def show_movie(id):
    movie = database.movie(id)
    credits = database.credits(id)
    response = render_template('movie.html',
                               movie=movie,
                               credits=credits)
    return response
