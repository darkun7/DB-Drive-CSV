
#!/usr/bin/env python
import os
from flask import Flask, render_template, request, json, send_from_directory
# import dbdrive as connect
from reader import *

app = Flask(__name__, template_folder='template')

@app.route("/")
def landingPage():
    return render_template("index.html")

@app.route("/",methods=['POST'])
def readCSV():
    res = csvreader.main(request)
    return res

@app.route("/xls",methods=['POST'])
def readXLS():
    res = xlsreader.main(request)
    return res

if __name__=="__main__":
    app.run(debug=True)