from flask import render_template, request, redirect
from app import app
from app.models.game import find_winner, computer_result
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

@app.route('/play')
def play():
    return render_template("play.html", find_winner=find_winner)

@app.route('/play', methods=['GET', 'POST'])
def cpu_game():
    choice1 = computer_result()
    choice2 = request.form['player_selection']
    name1 = request.form['player_name']
    player1 = Player("The Computer", choice1)
    player2 = Player(name1, choice2)
    find_winner(player1, player2)
    return redirect('/play')




    

