from flask import Flask
from models.login import loginpage
from models.disconnect import logout
from models.homepage import home
from models.gameitems import itemspage
from models.desc import descpage
from models.add import addpage
from models.edit import editpage
from models.delete import deletepage
from models.jsondata import jsonpage
from models.decorators import *
from models.dbconnect import *


app = Flask(__name__)
app.register_blueprint(loginpage)
app.register_blueprint(logout)
app.register_blueprint(home)
app.register_blueprint(itemspage)
app.register_blueprint(descpage)
app.register_blueprint(addpage)
app.register_blueprint(editpage)
app.register_blueprint(deletepage)
app.register_blueprint(jsonpage)


if __name__ == "__main__":
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
