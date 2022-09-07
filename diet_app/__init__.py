from multiprocessing.dummy import active_children
from flask import Flask, render_template, request, redirect, url_for,jsonify
from .views import search_route, menu_search, recipe

def create_app():
    app = Flask(__name__)
    app.register_blueprint(search_route.bp)
    app.register_blueprint(menu_search.bp)

    @app.route('/', methods = ['GET','POST'])
    def mainview():
        return render_template("home.html")


    return app

