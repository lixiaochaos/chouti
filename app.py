from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

import pymysql

app = Flask(__name__)
bootstrap =Bootstrap(app)

@app.route('/')
def index():
    conn = pymysql.connect(host='192.168.0.91', user='test', password='123456', db='chouti')
    cur = conn.cursor()
    #sql = "SELECT * FROM chouti"
    sql = "select *  from chouti order by id desc LIMIT 200"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('index.html', u=u)


if __name__ == '__main__':
    app.run()
