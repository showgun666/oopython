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
from src.leaderboard import Leaderboard
from src.sort import recursive_insertion
from src.queue import Queue

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

DEFAULT_PLAYERS_MAX = 4

@app.route("/")
def index():
    """ Index route """
    return render_template("index.html", session=session)

@app.route("/init", methods=["GET"])
def init():
    """ Intialize values needed in session """
    game_scoreboards = []
    for i in range(DEFAULT_PLAYERS_MAX):
        game_scoreboards.append(Scoreboard(i))
        session["rules" + str(i)] = game_scoreboards[i].get_rules()
        session["total_points" + str(i)] = game_scoreboards[i].get_total_points()

    game_hand = Hand()
    session["hand"] = game_hand.to_list()

    session["message"] = ""
    session["rerolls"] = 0
    session["finished"] = 0

    session["debug"] = ""

    session["player_amount"] = 1
    session["player_queue"] = [0]

    return redirect(url_for('main'))

@app.route("/main", methods=["GET"])
def main():
    """ Main route """
    # Create game objects from session
    player_amount = session["player_amount"]
    game_hand = Hand(session["hand"])
    game_scoreboards = []
    total_points = []
    rules_point_list = []
    finished = session["finished"]
    player_queue = Queue()

    # Queue
    if len(session["player_queue"]) != int(player_amount):
        for i in range(int(session["player_amount"])):
            player_queue.enqueue(i)
    else:
        for i in session["player_queue"]:
            player_queue.enqueue(i)
    session["player_queue"] = player_queue.to_list()

    # Current Player
    current_player = int(player_queue.peek())
    session["current_player"] = current_player

    # All scoreboards total points and rules
    for i in range(int(player_amount)):
        game_scoreboards.append(Scoreboard.from_dict(session["rules" + str(i)]))
        total_points.append(session["total_points" + str(i)])
        rules_point_list.append(list(game_scoreboards[i].get_rules().keys()))

    # Is finished
    if all(scoreboard.finished() for scoreboard in game_scoreboards):
        session["finished"] = 1
        finished = 1

    # Message
    if all(scoreboard.finished() for scoreboard in game_scoreboards):
        session["message"] = "Game finished! Final score: " + str(max(total_points)) + " points."
        session["finished"] = True
    message = session["message"]
    session["message"] = ""

    scored_points_dic = {}
    for rule in game_scoreboards[current_player].get_rules():
        scored_points_dic[rule] = game_scoreboards[current_player].get_rules()[rule]

    # Get points from each rule for current hand
    rule_values = {}
    for rule in game_scoreboards[current_player].rules_list:
        rule_values[rule.name] = rule.points(game_hand)

    # Returns value of every die in hand.
    return render_template(
        "main.html",
        dice1 = game_hand.dice[0].get_value(),
        dice2 = game_hand.dice[1].get_value(),
        dice3 = game_hand.dice[2].get_value(),
        dice4 = game_hand.dice[3].get_value(),
        dice5 = game_hand.dice[4].get_value(),
        rules = rules_point_list[current_player],
        points = scored_points_dic,
        rule_values = rule_values,
        total_points = total_points,
        message = message,
        finished = finished,
        player_amount = player_amount,
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
    player_queue = Queue()
    for i in session["player_queue"]:
        player_queue.enqueue(i)
    player = str(player_queue.peek())
    game_scoreboard = Scoreboard.from_dict(session["rules" + player])
    session["rules" + player] = game_scoreboard.get_rules()
    session["total_points" + player] = game_scoreboard.get_total_points()

    if game_scoreboard.get_points(request.args.get('rule')) == -1:
        game_scoreboard.add_points(request.args.get('rule'), game_hand)
        game_hand.roll()

        # Update Session
        session["rules" + player] = game_scoreboard.get_rules()
        session["hand"] = game_hand.to_list()
        session["total_points" + player] = game_scoreboard.get_total_points()
        session["rerolls"] = 0

        # Update the queue
        player = int(player_queue.dequeue())
        player_queue.enqueue(player)
        session["player_queue"] = player_queue.to_list()
    else:
        # Say the rule is already scored. Value stored in session
        session["message"] = request.args.get('rule') + " is already scored!"

    return redirect(url_for('main'))

@app.route("/enter_name_to_leaderboard", methods=["POST"])
def enter_name_to_leaderboard():
    """ Route for entering name to leaderboard """
    lb = Leaderboard.load("leaderboard.txt")
    pts = [
        session["total_points0"],
        session["total_points1"],
        session["total_points2"],
        session["total_points3"]
        ]
    points = max(pts)
    lb.add_entry(points, request.form.get("name"))
    lb.save("leaderboard.txt")
    return redirect(url_for('init'))

@app.route("/leaderboard")
def leaderboard():
    """ Route for viewing leaderboard """
    unsorted_entries = Leaderboard.load("leaderboard.txt")
    sorted_entries = recursive_insertion(Leaderboard.load("leaderboard.txt").entries, 1, True)

    sorted_leaderboard = Leaderboard()
    for i in range(sorted_entries.size()):
        sorted_leaderboard.add_entry(sorted_entries.get(i)[0], sorted_entries.get(i)[1])

    return render_template(
        "leaderboard.html",
        sorted_leaderboard=sorted_leaderboard,
        unsorted_leaderboard=unsorted_entries
        )

@app.route("/process_deletion", methods=["POST"])
def process_deletion():
    """ Process deletion of entry in leaderboard route """
    lb = Leaderboard.load("leaderboard.txt")
    lb.remove_entry(int(request.form["selected_index"]))
    lb.save("leaderboard.txt")

    return redirect(url_for('leaderboard'))

@app.route("/change_player_amount", methods=["POST"])
def change_player_amount():
    """ Change player amount route """
    session["player_amount"] = request.form["selected_number"]
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
