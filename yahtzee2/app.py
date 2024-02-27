#!/usr/bin/env python3
"""
Yahtzee app, html test module
"""
# Importera relevanta moduler
import os
import re
from flask import Flask, render_template, request, redirect, url_for, session
from src.hand import Hand
from src.scoreboard import Scoreboard

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

@app.route("/")
def index():
    """ Index route """
    return render_template("index.html")

@app.route("/init", methods=["GET"])
def init():
    """ Intialize values needed in session """
    game_scoreboard = Scoreboard()
    game_hand = Hand()

    session["rules"] = game_scoreboard.get_rules()
    session["hand"] = game_hand.to_list()
    session["total_points"] = game_scoreboard.get_total_points()
    session["message"] = ""
    session["rerolls"] = 0
    
    return redirect(url_for('main'))

@app.route("/main", methods=["GET"])
def main():
    """ Main route """
    # Create game objects from session
    game_hand = Hand(session["hand"])
    game_scoreboard = Scoreboard.from_dict(session["rules"])
    total_points = session["total_points"]

    if game_scoreboard.finished():
        session["message"] = "Game is already finished. Press Play or Reset to start a new game."

    # Get message from session
    if session["message"]:
        message = session["message"]
        session["message"] = ""
    else:
        message = ""

    rules_point_list = list(game_scoreboard.get_rules().keys())
    scored_points_dic = {}

    for rule in game_scoreboard.get_rules():
        scored_points_dic[rule] = game_scoreboard.get_rules()[rule]

    # Get values of each die
    d1 = game_hand.dice[0].get_value()
    d2 = game_hand.dice[1].get_value()
    d3 = game_hand.dice[2].get_value()
    d4 = game_hand.dice[3].get_value()
    d5 = game_hand.dice[4].get_value()

    # Get points from each rule for current hand
    rule_values = {}
    for rule in game_scoreboard.rules_list:
        rule_values[rule.name] = rule.points(game_hand)

    # Returns value of every die in hand.
    return render_template(
        "main.html",
        dice1 = d1,
        dice2 = d2,
        dice3 = d3,
        dice4 = d4,
        dice5 = d5,
        rules = rules_point_list,
        points = scored_points_dic,
        rule_values = rule_values,
        total_points = total_points,
        message = message
        )

@app.route("/roll_selected_dice", methods=["POST"])
def roll_selected_dice():
    """Roll selected dice route"""
    if session["rerolls"] < 2:
        game_hand = Hand(session["hand"])
        dice = [
            request.form.get("die1"),
            request.form.get("die2"),
            request.form.get("die3"),
            request.form.get("die4"),
            request.form.get("die5")
        ]

        i = len(dice)-1
        while i >= 0:
            if dice[i] is None:
                dice.pop(i)
            else:
                dice[i] = int(dice[i])
            i -= 1

        game_hand.roll(dice)
        session["hand"] = game_hand.to_list()
        session["rerolls"] += 1
    else:
        session["message"] = "Too many rerolls. Select a rule to score."

    return redirect(url_for('main'))

@app.route("/score_rule", methods=["GET"])
def score_rule():
    """ Score a rule route """
    game_hand = Hand(session["hand"])
    game_scoreboard = Scoreboard.from_dict(session["rules"])

    if game_scoreboard.get_points(request.args.get('rule')) == -1:
        # Add points
        game_scoreboard.add_points(request.args.get('rule'), game_hand)
        # Roll hand
        game_hand.roll()

        # Update Session
        session["rules"] = game_scoreboard.get_rules()
        session["hand"] = game_hand.to_list()
        session["total_points"] = game_scoreboard.get_total_points()
        session["rerolls"] = 0
    else:
        # Say the rule is already scored. Value stored in session
        session["message"] = request.args.get('rule') + " is already scored. Select a different rule."

    if game_scoreboard.finished():
        session["message"] = "Game finished with a Final score of " + str(game_scoreboard.get_total_points()) + " points.\nPress Reset or Play to start a new game of Yahtzee."
    return redirect(url_for('main'))

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html")

@app.route("/reset")
def reset():
    """ Route for reset session """
    _ = [session.pop(key) for key in list(session.keys())]

    return redirect(url_for('init'))

if __name__ == "__main__":
    app.run(debug=True)
