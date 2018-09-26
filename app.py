from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import long_long_ago, catz, cave_battle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def choose_story():
    """ """
    story_list=['long_long_ago','catz','cave_battle']

    return render_template('story.html', story_list=story_list)

@app.route('/words')
def collect_words():
    """ """

    story_chosen=request.args['stories']
    if story_chosen=='long_long_ago':
        words = long_long_ago.words

    if story_chosen=='catz':
        words = catz.words

    if story_chosen=='cave_battle':
        words = cave_battle.words

    return render_template('words.html', words=words,ultimate_story=story_chosen)


@app.route('/story')
def render_story():
    words_dict = {}

    story_chosen=request.args['story']
    if story_chosen=='long_long_ago':
        ultimate_story = long_long_ago

    if story_chosen=='catz':
        ultimate_story = catz

    if story_chosen=='cave_battle':
        ultimate_story = cave_battle

    for word in request.args:
       words_dict[word] = request.args.get(word)
    
    story_text = ultimate_story.generate(words_dict)
    
    return render_template('madlib.html', your_story=story_text)

