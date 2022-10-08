from venv import create
import json
import jsonify
import mysql.connector
from pickle import TRUE
from flask import Flask,jsonify,request

app=Flask(__name__)

data_base = mysql.connector.connect(host='127.0.0.1',
                                    user='root',
                                    passwd='mysql@1419',
                                    db='productdb',
                                    port=3306)

cursor = data_base.cursor(dictionary=True)

cursor.execute("SELECT * FROM productdb.products")

data_details = cursor.fetchall()

@app.route('/')
def index():
    return "Products Details"

@app.route("/details" , methods = ['GET'])
def get_all_details():
   return jsonify({'products':data_details})

@app.route("/details/<int:idProducts>",methods=['GET'])
def get_Products(idProducts):
    return jsonify({ 'products' : data_details[idProducts]})

if __name__=="__main__":
   app.run(debug=TRUE)