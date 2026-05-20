from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bankdb"
)

cursor = db.cursor()

# Show form
@app.route('/')
def form():
    return open("form.html").read()

# Insert data
@app.route('/insert', methods=['POST'])
def insert():
    acc_no = request.form['acc_no']
    name = request.form['name']
    balance = request.form['balance']

    sql = "INSERT INTO account VALUES (%s, %s, %s)"
    cursor.execute(sql, (acc_no, name, balance))
    db.commit()

    return "Record inserted successfully"

app.run(debug=True)