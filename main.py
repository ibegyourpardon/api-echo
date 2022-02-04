'''
Date: 2022-02-04 22:02:49
LastEditors: ibegyourpardon
LastEditTime: 2022-02-04 23:32:09
FilePath: /api-echo/main.py
'''
import json
import random
import string
from time import time
from turtle import st

from flask import Flask, jsonify
from flask import request


app = Flask(__name__)

store = []

def get_random_letter():
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return ran_str


def is_expired():
    for i in store:
        if i['expired'] == True:
            return True


@app.post('/')
def push():
    a = request.get_data()
    try:
        data = json.loads(a)
    except json.JSONDecodeError as e:
        return jsonify({"error": "json decode error"})
    else:
        hash = get_random_letter()
        item = {}
        item['code'] = 1
        item['created_at'] = int(time())
        item['hash'] = hash
        item['msg'] = 'success'
        item['data'] = data
        store.append(item)

    for i in store:
        if int(time()) - i['created_at'] > 60 * 60 * 24:
            store.remove(i)

    return jsonify(item)



@app.get('/<hash>')
def echo(hash):
    for item in store:
        if item['hash'] == hash:
            return jsonify(item['data'])
    return jsonify({"error": "not found"})

#app.run(debug=True, host='localhost', port=5009)