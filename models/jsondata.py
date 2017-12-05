from flask import Flask, Blueprint, jsonify
from models.dbconnect import *


jsonpage = Blueprint("jsonpage", __name__)


# JSON API to view Catalog Information
@jsonpage.route('/catalog.json')
def allGamesJSON():
    """
    Returns json data of all games and their items stored in the database
    """
    games = session.query(Game).all()
    result = [i.serialize for i in games]
    data = {"Category": result}
    for i in games:
        gameitems = session.query(GameItem).filter_by(game_id=i.id).all()
        items = [j.serialize for j in gameitems]
        result[i.id-1]["Items"] = items
    return jsonify(data)
