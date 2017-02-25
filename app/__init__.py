from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
Bootstrap(app)

from .serch.views import serch as serchModule
app.register_blueprint(serchModule)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translait')
def translait():
    return render_template('translait.html')
