# -*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from src.view import bp
from config import cfg
app = Flask(__name__)
app.secret_key = cfg.get('params','').get('secret_key','')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = cfg.get('params','').get('SQLALCHEMY_TRACK_MODIFICATIONS','')
app.config['SQLALCHEMY_DATABASE_URI'] = cfg.get('params','').get('SQLALCHEMY_DATABASE_URI','')
# set default button sytle and size, will be overwritten by macro parameters
app.config['BOOTSTRAP_BTN_STYLE'] = cfg.get('params','').get('BOOTSTRAP_BTN_STYLE','')
app.config['BOOTSTRAP_BTN_SIZE'] = cfg.get('params','').get('BOOTSTRAP_BTN_SIZE','')

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
print(db)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()
