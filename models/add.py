from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask import flash
from models.dbconnect import *
from models.login import login_session
from models.decorators import *


addpage = Blueprint("addpage", __name__)


# Creating a new Item
@addpage.route('/catalog/add(logged in)/', methods=['GET', 'POST'])
@login_required
def addNewItem():
    """
    Adding the new item details to the database and returning back to homepage
    """
    if request.method == 'POST':
        user_id = login_session['user_id']
        game_name = request.form['category']
        game = session.query(Game).filter_by(name=game_name).first()
        new_item = GameItem(name=request.form['name'],
                            description=request.form['desc'], game_id=game.id,
                            user_id=user_id)
        session.add(new_item)
        session.commit()
        flash("Game Item Added Succesfully")
        return redirect(url_for('home.allGames'))
    else:
        games = session.query(Game).all()
        return render_template('addnewitem.html', all_games=games)
