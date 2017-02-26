from flask import Blueprint, render_template, redirect, request, url_for

serch = Blueprint('serch', __name__, template_folder="templates")

@serch.route('/gurgleSerch')
def gurgleSerch():
    query = request.args.get('query')
    print(query)
    if(query==""):
        return redirect(url_for('index'))
    return render_template('serch.html', query=query)
