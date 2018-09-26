from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def collect_words():
    words = story.words

    return render_template('words.html', words=words)


@app.route('/story')
def render_story():
    words_dict = {}
    for word in request.args:
       words_dict[word] = request.args.get(word)
    story_text = story.generate(words_dict)
    return render_template('madlib.html', your_story=story_text)

