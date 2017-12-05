from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask import flash
from models.dbconnect import *
from models.login import login_session
from models.decorators import *


deletepage = Blueprint("deletepage", __name__)


# Delete an item
@deletepage.route('/catalog/<game_name>/<item_name>/delete(logged in)/',
                  methods=['GET', 'POST'])
@login_required
@check_item
@check_owner
def deleteItem(game_name, item_name):
    """
    Allows logged in users to delete item from database created by them only.
    """
    game = session.query(Game).filter_by(name=game_name).first()
    itemToDelete = session.query(GameItem).filter(and_(GameItem.name ==
                                                       item_name,
                                                       GameItem.game_id ==
                                                       game.id)).first()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Game Item Successfully Deleted')
        return redirect(url_for('itemspage.gameItems', game_name=game.name))
    else:
        return render_template('deleteitem.html', item=itemToDelete)
