from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# mysql setup
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

mysql = MySQL(app)

# halaman index
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bahaya-masturbasi')
def bahaya():
    v = 1
    if v == 1:
        return redirect(url_for('index'))
    return render_template('bahaya.html')

# halaman untuk melihat database
@app.route('/lihat')
def lihat():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    data = cur.fetchall()
    return render_template('lihat.html', user = data)

# method untuk memasukan data username dan password ke database mysql
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
