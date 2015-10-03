import flask
from flask import Flask, redirect, request
import sqlite3
import json
import sys
from firebase import Firebase
from flask import g
import requests.packages.urllib3
app = Flask(__name__)


@app.route('/')
def index():
	return flask.render_template('index.html')

@app.route('/register')
def register():
	return flask.render_template('register.html')

@app.route('/info')
def info():
	return flask.render_template('info.html')

@app.route('/submit', methods=['POST'])
def store_data():
	#db=sqlite3.connect('database.db');
	#curs = db.cursor()
	#curs.execute('CREATE TABLE Shelter(user TEXT, email TEXT, phone TEXT, comment TEXT, duration TEXT );')
	f = Firebase('https://shelterx2.firebaseio.com/data')
	t_usr=request.form['usr']
	t_email=request.form['email']
	t_phone=request.form['phone']
	t_description=request.form['description']
	t_duration=request.form['duration']
	t_country=request.form['country']
	t_city=request.form['city']
	f.push({'name':t_usr,'email':t_email,'phone':t_phone,'description':t_description,'duration':t_duration, 'country':t_country, 'city':t_city})
	#curs.execute('INSERT INTO Shelter (user,email,phone,comment,duration) VALUES (?,?,?,?,?);',(t_usr,t_email,t_phone,t_comment,t_duration))
	#db.commit()
	#db.close()
	return redirect('/')


@app.route('/main')
def main():
	#db=sqlite3.connect('database.db')
	#curs = db.cursor()
	#db.execute("SELECT * FROM Shelter")
	#recs = db.fetchall()
	#print recs
	#rows=[dict(rec) for rec in recs]
	#print rows
	#rows_json=json.dumps(curs)
	#f=open('json_db', 'w') 
	#print >> f,rows_json
	#db.close()
	return flask.render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
