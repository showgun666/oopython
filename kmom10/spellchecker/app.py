#!/usr/bin/env python3
"spellchecker app main"
import os
import re
from flask import Flask, render_template, request, redirect, url_for, session
from src.trie import Trie

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

@app.route("/init", methods=["GET"])
def init():
    """ Intialize values needed in session """
    removed_words = [] # Holds a list of items in order that have been removed to the dictionary.
    session["removed_words"] = removed_words
    return redirect(url_for('main'))

@app.route("/", methods=["GET"])
def main():
    "Main route"
    removed_words = [] # Holds a list of items in order that have been removed to the dictionary.
    current_word_list = "dictionaries/dictionary.txt"
    session["removed_words"] = removed_words
    session["current_word_list"] = current_word_list
    session["prefix_search"] = ""
    return render_template("index.html"
                           )


@app.route("/all-words", methods=["GET"])
def all_words():
    "All-words Route"
    dictionary_trie = Trie.create_from_file(session["current_word_list"])
    for entry in session["removed_words"]:
        dictionary_trie.remove_word(entry)
    return render_template("all-words.html",
                           word_count = dictionary_trie.count_words(),
                           words_list = dictionary_trie.get_words()
                           )


@app.route("/prefix-search")
def prefix_search():
    "prefix-search Route"
    prefix = session["prefix_search"]
    prefix_search_words = ""

    if len(prefix) > 0:
        dictionary_trie = Trie.create_from_file(session["current_word_list"])
        for entry in session["removed_words"]:
            dictionary_trie.remove_word(entry)
        prefix_search_words = dictionary_trie.prefix_search(prefix)

    return render_template("prefix-search.html", input = prefix,
                           prefix_search_words = prefix_search_words
                           )
@app.route("/prefix-search-trie", methods=["POST"])
def prefix_search_trie():
    "prefix_search_trie Route"
    session["prefix_search"] = request.form.get("word")
    return redirect(url_for("prefix_search"))


@app.route("/find-word")
def find_word():
    "find-word Route"
    word_found = None
    if session["word_found"] is not None:
        word_found = session["word_found"]
    word_to_find = session["word_to_find"]
    session["word_found"] = None
    session["word_to_find"] = None
    return render_template("find-word.html",
                           word_found = word_found,
                           word_to_find = word_to_find,
                           )
@app.route("/find-word-in-trie", methods=["POST"])
def find_word_in_trie():
    "find-word Route"
    dictionary_trie = Trie.create_from_file(session["current_word_list"])
    for entry in session["removed_words"]:
        dictionary_trie.remove_word(entry)

    word_to_find = request.form.get("word")
    session["word_to_find"] = word_to_find
    session["word_found"] = dictionary_trie.find_word(word_to_find)
    return redirect(url_for("find_word"))


@app.route("/remove-word")
def remove_word():
    "remove-word Route"
    return render_template("remove-word.html",
                           )
@app.route("/remove-word-from-trie", methods=["POST"])
def remove_word_from_trie():
    "remove-word-from-trie Route"
    dictionary_trie = Trie.create_from_file(session["current_word_list"])
    word_to_remove = request.form.get("word")
    dictionary_trie.remove_word(word_to_remove) # CAN'T HANDLE EXCEPTION

    # Add word to session
    removed_words = []
    for word in session["removed_words"]:
        removed_words.append(word)
    removed_words.append(word_to_remove)
    session["removed_words"] = removed_words

    return redirect(url_for('remove_word'))


@app.route("/select-word-list")
def select_word_list():
    "select-word-list Route"
    return render_template("select-word-list.html",
                           )
@app.route("/change-word-list", methods=["POST"])
def change_word_list():
    "change-word-list Route"
    session["current_word_list"] = request.form.get("word_list")
    session["removed_words"] = []
    return redirect(url_for('select_word_list'))


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
