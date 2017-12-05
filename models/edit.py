from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask import flash
from models.dbconnect import *
from models.login import login_session
from models.decorators import *


editpage = Blueprint("editpage", __name__)


# Edit an Item
@editpage.route('/catalog/<game_name>/<item_name>/edit(logged in)/',
                methods=['GET', 'POST'])
@login_required
@check_item
@check_owner
def editItem(game_name, item_name):
    """
    Allows logged in users to modify item details in the database created by
    them only.
    """
    selected_game = session.query(Game).filter_by(name=game_name).first()
    edited_item = session.query(GameItem).filter(and_(GameItem.name ==
                                                      item_name,
                                                      GameItem.game_id ==
                                                      selected_game.id
                                                      )).first()
    if request.method == 'POST':
        if request.form['new_name'] != '':
            edited_item.name = request.form['new_name']
        if request.form['new_desc'] != '':
            edited_item.description = request.form['new_desc']
        if request.form['new_category'] != '':
            new_game = session.query(Game).filter_by(
                name=request.form['new_category']).first()
            edited_item.game_id = new_game.id
        session.add(edited_item)
        session.commit()
        flash("Game Item Edited Succesfully")
        return redirect(url_for('home.allGames'))
    else:
        games = session.query(Game).all()
        return render_template('edititem.html', all_games=games,
                               item=edited_item)
