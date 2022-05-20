import pandas as pd
from flask import jsonify
import pandas as pd
import requests
from io import StringIO

def formating(column, df):
    records = []
    res = df.to_numpy().tolist()
    print(res)
    for _ in range(len(res)):
        item = {}
        for __ in range(len(column)):
            attribute = column[__]
            value = res[_][__]
            item[attribute] = str(value)
        records.append(item)
    return records

def stream(uri):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}
    req = requests.get(uri, headers=headers)
    data = StringIO(req.text)
    return data


def main(index, identifier, df):
    column = df.columns
    
    if (index is None):
        record = formating(column, df)
        return jsonify({"response": record, "message":"Success"}), 200
    try:
        index = int(index) if index.isdigit() else index
        res = df.loc[df[str(identifier)] == index]
    
        if not res.empty:
            record = formating(column, res)
            return jsonify({"response": record, "message":"Success"}), 200
        else:
            return jsonify({"response": None, "message":"No Record"}), 404
    except KeyError:
        return jsonify({"response": None, "message":"Identifier may typo or doesn't exist"}), 400
    except Exception as e:
        return jsonify({"response": None, "message":e}), 500