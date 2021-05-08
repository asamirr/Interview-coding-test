import sqlite3
import os.path
import click
from flask import current_app, g
from flask.cli import with_appcontext

DATABASE = '../pythonsqlite.db'

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "pythonsqlite.db")

def get_db():
    db= sqlite3.connect(DATABASE, timeout=3)
    db.row_factory = sqlite3.Row

    return db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource(os.getcwd() + '/model/myschema.sql') as f:
        db.executescript(f.read().decode('utf8')) 

def place_a_bid(petID, amount, userID):
    db = get_db()
    db_cursor = db.cursor().execute(
        '''Insert into BIDS (petID, amount, userID) values (?,?,?)''', 
        (petID, amount, userID))
    db.commit()
    db.close()

def list_bids():
    db = get_db()
    bids = db.cursor().execute(
        'SELECT * FROM BIDS')
    all = []
    for bid in bids:
        dic = {
            'petID': bid['petID'],
            'amount': bid['amount'],
            'userID': bid['userID']
        }
        all.append(dic)
    db.close()
    return all