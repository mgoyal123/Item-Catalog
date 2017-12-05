from flask import Flask, render_template, redirect, url_for, Blueprint
from flask import flash
from models.dbconnect import *
from models.login import login_session
from models.decorators import *


itemspage = Blueprint("itemspage", __name__)


# Show a list of all games with items of selected game
@itemspage.route('/catalog/<game_name>/items')
@check_game
def gameItems(game_name):
    """
    Shows a list of all games on left pane and a list of game items of clicked
    game on the right pane
    """
    if 'username' not in login_session:
        games = session.query(Game).all()
        selected_game = session.query(Game).filter_by(name=game_name).first()
        game_items = session.query(GameItem).filter_by(
            game_id=selected_game.id).all()
        return render_template('publicgameitems.html', all_games=games,
                               items=game_items)
    else:
        return redirect(url_for('itemspage.gameItemsLoggedin',
                                game_name=game_name))


# Show a list of all games and items of selected game with Add item option
@itemspage.route('/catalog/<game_name>/items(logged in)/')
@login_required
@check_game
def gameItemsLoggedin(game_name):
    """
    Shows a list of all games on left pane and a list of game items of clicked
    game on the right pane with an Add item option for logged in users
    """
    games = session.query(Game).all()
    selected_game = session.query(Game).filter_by(name=game_name).first()
    game_items = session.query(GameItem).filter_by(
        game_id=selected_game.id).all()
    return render_template('gameitems.html', all_games=games,
                           items=game_items)
