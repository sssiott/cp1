from flask import Blueprint
from flask import render_template, request
import sqlite3

bp = Blueprint('menu_search', __name__, url_prefix='/menu')

@bp.route('/', methods = ['GET','POST'])
def print_recipe():
    menu_name = request.args.get('menu')
    conn = sqlite3.connect('diet_app/test.db')
    cur = conn.cursor()
    a = cur.execute(f'SELECT m.menu ,m.views,m.category , SUM(price) FROM menu m JOIN reicpe r ON m.menu = r.menu  JOIN ingredient i ON i.name = r.ingred GROUP BY m.menu HAVING m.menu LIKE "%{menu_name}%";')
    return render_template('menu_search.html', menu = menu_name, li=a)
