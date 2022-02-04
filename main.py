'''
Date: 2022-02-04 22:02:49
LastEditors: ibegyourpardon
LastEditTime: 2022-02-05 00:05:50
FilePath: /api-echo/main.py
'''
import json
import random
import string
from time import time

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

store = []


def get_random_letter():
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return ran_str


def is_expired():
    for i in store:
        if i['expired']:
            return True


@app.post('/')
def push():
    a = request.get_data()
    try:
        data = json.loads(a)
    except json.JSONDecodeError as e:
        return jsonify({"error": "json decode error"})
    else:
        hash_str = get_random_letter()
        item = {'code': 1, 'created_at': int(time()), 'hash': hash_str, 'msg': 'success', 'data': data}
        store.append(item)

    for i in store:
        if int(time()) - i['created_at'] > 60 * 60 * 24:
            store.remove(i)

    return jsonify(item)


@app.get('/<hash_str>')
def echo(hash_str):
    for item in store:
        if item['hash'] == hash_str:
            return jsonify(item['data'])
    return jsonify({"error": "not found"})

# app.run(debug=True, host='localhost', port=5009)
