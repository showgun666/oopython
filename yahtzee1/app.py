#!/usr/bin/env python3
"""
Yahtzee app, html test module
"""
# Importera relevanta moduler
from flask import Flask, render_template
import src.die as die
import src.hand as hand
import random

app = Flask(__name__)

@app.route("/")
def index():
    """ Index route """
    return render_template("index.html")

@app.route("/main")
def main():
    """ Main route """
    # Create a hand.
    gameHand = hand.Hand()

    # Returns every die rolled once.
    return render_template("main.html", dice1 = gameHand.roll(1), dice2 = gameHand.roll(2), dice3 = gameHand.roll(3), dice4 = gameHand.roll(4), dice5 = gameHand.roll(5))

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)