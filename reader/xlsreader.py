import dbdrive as connect
import pandas as pd
from flask import jsonify

def main(request):
    index = request.form.get("index")
    identifier = request.form.get("identifier")
    xls = request.form.get("xls")

    if (xls is None):
        return jsonify({"response": None, "message": "Invalid xls URI"})
    if (identifier is None):
        return jsonify({"response": None, "message": "Invalid Identifier"})
    
    path = 'https://docs.google.com/spreadsheets/d/' + xls.split('/')[-2]  + '/export'
    df = pd.read_excel(connect.stream(path))

    return connect.main(index, identifier, df)