from flask_app import app 
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas/new')
def new_ninja():
    dojos = Dojo.get_all_dojos() 
    return render_template('new_ninjas.html', dojos = dojos)

@app.route('/create_ninja', methods=['POST']) 
def create_ninja():
    data = {
        'dojos_id':request.form['dojos_id'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age']
    }
    Ninja.create_ninja(data) 
    return redirect('/dojos')

