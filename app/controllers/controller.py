from flask import render_template
from app import app
from app.models.game import game
from app.models.player import Player

@app.route('/game')
def index():
    return "Let's play a game!"