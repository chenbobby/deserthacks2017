from flask import Blueprint, render_template, redirect, url_for

serch = Blueprint('serch', __name__, template_folder="templates")

def gurgleSerch(query):
    print(query)

