from flask import render_template
from app import app
from app.models.game import find_winner
from app.models.player import Player

@app.route('/game')
def index():
    return render_template("index.html")

@app.route('/<choice1>/<choice2>')
def play_game(choice1, choice2):
    player1 = Player("Little Richard", choice1)
    player2 = Player("Glenn Danzig", choice2)
    get_result = find_winner(player1, player2)
    return render_template('index.html', result=get_result)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")
    

    

