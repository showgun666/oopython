#!/usr/bin/env python3
"""
Main applikation for website
"""
import os
import re
from src.guess_game import GuessGame
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@app.route("/init", methods=["GET"])
def init():
    """ Intialize values needed in session """
    game = GuessGame()
    session["correct"] = game.get_correct_value()
    session["guesses"] = game.to_list()
    return redirect(url_for('guess'))

@app.route("/guess", methods=["GET"])
def guess():
    """Main view for game"""
    game = GuessGame(session["correct"], session["guesses"])
    return render_template("guess.html", game=game)

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()

@app.route("/check-guess", methods=["POST"])
def check_guess():
    """Make a new guess with users form value"""
    game = GuessGame(session["correct"], session["guesses"])
    guess = int(request.form.get("value"))
    game.make_guess(guess)
    session["guesses"] = game.to_list()
    return redirect(url_for('guess'))

@app.route("/reset")
def reset():
    """ Route for reset session """
    _ = [session.pop(key) for key in list(session.keys())]

    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)
