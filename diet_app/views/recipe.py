from flask import Blueprint
from flask import render_template, request
import sqlite3

bp = Blueprint('print_recipe', __name__, url_prefix='/recipe')

@bp.route('/', methods = ['GET','POST'])
def print_recipe():
    menu_name = request.args.get('menu')
    return render_template('print_recipe.html', menu = menu_name )
