#!/usr/bin/env python3
"""
Yahtzee app, html test module
"""
# Importera relevanta moduler
from flask import Flask, render_template
from src.hand import Hand

app = Flask(__name__)

@app.route("/")
def index():
    """ Index route """
    return render_template("index.html")

@app.route("/main")
def main():
    """ Main route """
    # Create a hand.
    gamehand = Hand()
    # Rolls 5 dice
    gamehand.roll()
    # Get values of each die
    d1 = gamehand.dice[0].get_value()
    d2 = gamehand.dice[1].get_value()
    d3 = gamehand.dice[2].get_value()
    d4 = gamehand.dice[3].get_value()
    d5 = gamehand.dice[4].get_value()

    # Returns value of every die in hand.
    return render_template("main.html", dice1 = d1, dice2 = d2, dice3 = d3, dice4 = d4, dice5 = d5)

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
