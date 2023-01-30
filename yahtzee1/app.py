#!/usr/bin/env python3
"""
Yahtzee app, html test module
"""
# Importera relevanta moduler
from flask import Flask, render_template
from src.die import Die
from src.hand import Hand
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
    gameHand = Hand()
    # Rolls 5 dice
    gameHand.roll(5)

    # Returns value of every die in hand.
    return render_template("main.html", dice1 = gameHand.dice[0].get_value(), dice2 = gameHand.dice[1].get_value(), dice3 = gameHand.dice[2].get_value(), dice4 = gameHand.dice[3].get_value(), dice5 = gameHand.dice[4].get_value())

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)