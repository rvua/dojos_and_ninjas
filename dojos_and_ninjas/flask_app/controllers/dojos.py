from flask_app import app 
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def index_dojos():
    all_dojos = Dojo.get_dojos_with_ninjas()
    return render_template('dojos.html', all_dojos = all_dojos)

@app.route('/new_dojo', methods=["POST"])
def new_dojo():
    data = {
        'name':request.form['dname']
    }
    Dojo.create_dojo(data) 
    return redirect('/dojos')

@app.route('/city/ninjas/<int:dojos_id>')
def show_dojo(dojos_id):
    data = {
        'dojos_id': dojos_id
    }
    dojo = Dojo.get_dojo(data)
    return render_template('dojo_city.html', dojo = dojo)