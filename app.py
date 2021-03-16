from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)

app.config['SECRET_KEY'] = "MissMillieIsGood"
debug = DebugToolbarExtension(app)

@app.route('/form')
def fill_out():
    return render_template("form.html")

@app.route('/story')
def show_story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    story= Story(["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
    your_story = story.generate({
        "place":place, 
        "noun":noun, 
        "verb":verb, 
        "adjective":adjective,
        "plural_noun":plural_noun})
    return render_template("story.html", story=your_story, place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)

@app.route('/test-story')
def test_story():
    new_story = Story(["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
    return new_story.generate({"place":"zoo","noun":"cat","verb":"run","adjective":"red","plural_noun":"dogs"})
