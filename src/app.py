from flask import Flask, request, render_template, Response
import psycopg2
import psycopg2.extras
import csv
import json
from psycopg2.extras import RealDictCursor
import requests

conn = psycopg2.connect("host='postgresql' port='5432' dbname='demo' user='postgres' password='somepassword'")
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    cur = conn.cursor()
    query = request.form['query']
    cur.execute(query)
    return Response(json.dumps(cur.fetchall(),indent=2),mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

# conn.close()
