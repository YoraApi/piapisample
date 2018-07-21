from flask import Flask, jsonify
from flaskext.mysql import MySQL
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'yoratech_admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Yora@335'
app.config['MYSQL_DATABASE_DB'] = 'yoratech_flaskapi_sample'
app.config['MYSQL_DATABASE_HOST'] = '45.114.79.179'

mysql.init_app(app)

@app.route('/')
def get():
    cur = mysql.connect().cursor()
    cur.execute('''select * from yoratech_flaskapi_sample.MyGuests''')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'myCollection' : r})

if __name__ == '__main__':
    app.run()