from flask import Blueprint, render_template, redirect, url_for

serch = Blueprint('serch', __name__, template_folder="templates")

@serch.route('/gurgleSerch', methods=['POST'])
def gurgleSerch():
    print("Gurgle Searched")
    return render_template('serch.html')
