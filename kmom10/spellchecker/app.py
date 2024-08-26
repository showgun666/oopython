#!/usr/bin/env python3
"spellchecker app main"
import os
import re
from flask import Flask, render_template, request, redirect, url_for, session
from src.trie import Trie

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

@app.route("/", methods=["GET"])
def main():
    "Main route"
    dictionary_trie = Trie.create_from_file("dictionaries/tiny_dictionary.txt")
    return render_template("index.html"
                           )

@app.route("/all-words", methods=["GET"])
def all_words():
    "All-words Route"
    dictionary_trie = Trie.create_from_file("dictionaries/tiny_dictionary.txt")
    return render_template("all-words.html",
                           word_count = dictionary_trie.count_words(),
                           words_list = dictionary_trie.get_words()
                           )

@app.route("/remove-word", methods=["POST"])
def remove_word():
    "remove-word Route"
    return render_template("remove-word.html",
                           )

@app.route("/remove-word-from-trie", methods=["GET"])
def remove_word_from_trie():
    "remove-word-from-trie Route"
    dictionary_trie = Trie.create_from_file("dictionaries/tiny_dictionary.txt")
    return redirect(url_for('remove-word.html'))

@app.route("/init", methods=["GET"])
def init():
    """ Intialize values needed in session """
    removed_words = [] # Holds a list of items in order that have been removed to the dictionary.
    session["removed_words"] = removed_words
    return redirect(url_for('main'))

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

if __name__ == "__main__":
    app.run(port=8080, debug=True)
