# search_route.py
from multiprocessing import connection
from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask import Blueprint
import sqlite3

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/',methods = ['GET','POST'])
def search():
    ingredients = request.form['ingredients']
    price = request.form['price']
    category = request.form['category']
    dislike = request.form['dislike']
    conn = sqlite3.connect('diet_app/test.db')
    cur = conn.cursor()
    a = cur.execute(f'SELECT r.menu , SUM(price) FROM reicpe r  JOIN ingredient i ON r.ingred = i.name GROUP BY menu HAVING SUM(price) <= {price}')
    # b = cur.execute('SELECT  r.menu, r.ingred, m.category, m.views FROM reicpe r  JOIN ingredient i ON r.ingred = i.name JOIN menu m ON m.menu = r.menu;')
    
    
    return render_template('result.html', price = price,dislike=dislike,  enumerate=enumerate, a=a)

