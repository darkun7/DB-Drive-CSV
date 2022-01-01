import pandas as pd
from flask import jsonify

def formating(column, df):
    records = []
    res = df.to_numpy().tolist()
    print(res)
    for _ in range(len(res)):
        item = {}
        for __ in range(len(column)):
            attribute = column[__]
            value = res[_][__]
            item[attribute] = value
        records.append(item)
    return records


def main(index, identifier, df):

    column = df.columns
    
    if (index is None):
        record = formating(column, df)
        return jsonify({"response": record, "message":"Success"})
    
    res = df.loc[df[str(identifier)] == int(index)]
    if res.empty:
        return jsonify({"response": None, "message":"No Record"})
    else:
        record = formating(column, res)
        return jsonify({"response": record, "message":"Success"})
    