#!/usr/bin/env python3
"""
Yahtzee app, html test module
"""
# Importera relevanta moduler
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/main")
def main():
    """ Main route """
    return render_template("main.html", dice1 = random.randint(1, 6), dice2 = random.randint(1, 6), dice3 = random.randint(1, 6), dice4 = random.randint(1, 6), dice5 = random.randint(1, 6))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)