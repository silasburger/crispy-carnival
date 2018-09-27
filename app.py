from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story_list

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def choose_story():
    """ """

    return render_template('story.html', story_list=story_list.keys())

@app.route('/words')
def collect_words():
    """ """

    story_chosen = request.args['stories']
    words = story_list[story_chosen].words
    
    return render_template('words.html', words=words,ultimate_story=story_chosen)


@app.route('/story')
def render_story():
    """ """
    words_dict = {}

    story_chosen=request.args['story']
    ultimate_story = story_list[story_chosen]

    for word in request.args:
       words_dict[word] = request.args.get(word)
    
    story_text = ultimate_story.generate(words_dict)
    
    return render_template('madlib.html', your_story=story_text)

