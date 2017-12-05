from flask import Flask, render_template, redirect, url_for
from models.dbconnect import *
from models.login import login_session
import functools


def check_game(func):
    @functools.wraps(func)
    def wrapper(game_name):
        game = session.query(Game).filter_by(name=game_name).first()
        if game:
            return func(game_name)
        else:
            return render_template('error.html')
    return wrapper


def check_item(func):
    @functools.wraps(func)
    def wrapper(game_name, item_name):
        game = session.query(Game).filter_by(name=game_name).first()
        if game:
            item = session.query(GameItem).filter(and_(GameItem.name ==
                                                       item_name,
                                                       GameItem.game_id ==
                                                       game.id)).first()
            if item:
                return func(game_name, item_name)
            else:
                return render_template('error.html')
        else:
            return render_template('error.html')
    return wrapper


def check_owner(func):
    @functools.wraps(func)
    def wrapper(game_name, item_name):
        game = session.query(Game).filter_by(name=game_name).first()
        item = session.query(GameItem).filter(and_(GameItem.name == item_name,
                                                   GameItem.game_id ==
                                                   game.id)).first()
        if item.user_id == login_session['user_id']:
            return func(game_name, item_name)
        else:
            return render_template('notauthorized.html')
    return wrapper


def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in login_session:
            return redirect(url_for('login.showLogin'))
        else:
            return func(*args, **kwargs)
    return wrapper
