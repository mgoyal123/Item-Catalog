from flask import Flask, render_template, redirect, url_for, Blueprint
from flask import flash
from models.login import login_session
from models.decorators import *
from dbconnect import *


home = Blueprint("home", __name__)


# Show list of all games and latest items
@home.route('/')
@home.route('/catalog/')
def allGames():
    """
    Shows the list of all games on left side and list of latest game items
    added on right side of the page
    """
    if 'username' not in login_session:
        games = session.query(Game).all()
        latest_items = session.query(GameItem).order_by(
            GameItem.id.desc()).limit(9).all()
        return render_template('publicgames.html', all_games=games,
                               latest_items=latest_items)
    else:
        return redirect(url_for('home.allGamesLoggedin'))


# Show list of all games and latest items with add item option
@home.route('/catalog(logged in)/')
@login_required
def allGamesLoggedin():
    """
    Shows a list of all games and latest game items added along with an Add
    item option at the top only for logged in users.
    """
    games = session.query(Game).all()
    latest_items = session.query(GameItem).order_by(
        GameItem.id.desc()).limit(9).all()
    return render_template('games.html', all_games=games,
                           latest_items=latest_items)
