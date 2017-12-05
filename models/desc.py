from flask import Flask, render_template, redirect, url_for, Blueprint
from flask import flash
from models.dbconnect import *
from models.login import login_session
from models.decorators import *


descpage = Blueprint("descpage", __name__)


# Show Description of selected item
@descpage.route('/catalog/<game_name>/<item_name>/')
@check_item
def itemDesc(game_name, item_name):
    """
    Show the description of a selected item
    """
    if 'username' not in login_session:
        selected_game = session.query(Game).filter_by(name=game_name).first()
        selected_item = session.query(GameItem).filter(and_(GameItem.name ==
                                                            item_name,
                                                            GameItem.game_id ==
                                                            selected_game.id
                                                            )).first()
        return render_template('publicgameitemdesc.html', item=selected_item)
    else:
        return redirect(url_for('descpage.itemDescLoggedin',
                                game_name=game_name, item_name=item_name))


# Show description of selected item with Edit and delete option
@descpage.route('/catalog/<game_name>/<item_name>/(logged in)/')
@login_required
@check_item
def itemDescLoggedin(game_name, item_name):
    """
    Show the description of a selected item along with Edit and Delete option
    only for users who created that particular item
    """
    selected_game = session.query(Game).filter_by(name=game_name).first()
    selected_item = session.query(GameItem).filter(and_(GameItem.name ==
                                                        item_name,
                                                        GameItem.game_id ==
                                                        selected_game.id
                                                        )).first()
    if login_session['user_id'] != selected_item.user_id:
        return render_template('publicgameitemdesc.html', item=selected_item)
    else:
        return render_template('gameitemdesc.html', item=selected_item)
