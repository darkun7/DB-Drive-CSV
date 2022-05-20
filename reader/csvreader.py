import dbdrive as connect
import pandas as pd
from flask import jsonify

def main(request):
    index = request.form.get("index")
    identifier = request.form.get("identifier")
    csv = request.form.get("csv")

    if (csv is None):
        return jsonify({"response": None, "message": "Invalid CSV URI"})
    if (identifier is None):
        return jsonify({"response": None, "message": "Invalid Identifier"})

    path = 'https://drive.google.com/uc?export=download&id=' + csv.split('/')[-2] 
    df = pd.read_csv(connect.stream(path))

    return connect.main(index, identifier, df)