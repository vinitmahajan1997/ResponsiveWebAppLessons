from app import app
from flask import render_template, request, redirect, flash, jsonify
import json

@app.route('/')
def items():
    user = {'owner': 'BC'}

    items = [
        {
            'item': 'Sugar',
            'discription' : 'White'
        },
        {
            'item': 'Rice',
            'discription': 'Basmati'
        }
    ]
    return render_template('OwnerPage.html', title='Home', user=user, items=items)


@app.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
    message = ""
    if request.method == "POST":
        username = request.json['username']
        if username == 'vinit':
            return "Success"
        else:
           message = "Not registred"
        return message
    else:
        return render_template('LoginPageMod.html')


@app.route('/process-data', methods=['POST'])
def process_data():
    data = request.json['data']
    return data


@app.route('/pro')
def look():
    return render_template('fetchdemo.html')


@app.route('/responsive', methods=['GET'])
def callResponsive():
    return render_template('ResponsiveBootS.html')


@app.route('/loginpop', methods=['GET', 'POST'])
def loginpop():
    error = None
    if request.method == 'POST':
        flash('You were successfully logged in')
        return render_template('layout.html', error=error)
    return render_template('layout.html', error=error)


