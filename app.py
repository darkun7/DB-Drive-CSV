
#!/usr/bin/env python
import os
from flask import Flask, render_template, request, json, send_from_directory
import dbdrive as connect

app = Flask(__name__, template_folder='template')

@app.route("/")
def landingPage():
    return render_template("index.html")

@app.route("/",methods=['POST'])
def readDB():
    res = connect.main(request)
    return res

if __name__=="__main__":
    app.run(debug=True)