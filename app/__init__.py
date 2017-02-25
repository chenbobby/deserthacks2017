from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def index():
    return render_template('index.html')
