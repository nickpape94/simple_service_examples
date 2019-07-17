#!flask/bin/python
from flask import Flask, jsonify, make_response
import sys
import requests
import string
import random

from random import randint
app = Flask(__name__)

@app.route('/test2', methods=['GET'])
def test2():
  my_string2 = "abcdefghijklmnopqrstuvwxyz"
  index1 = random.randint(0,25)
  index2 = random.randint(0,25)
  index3 = random.randint(0,25)
  letter3 = my_string2[index1]
  letter4 = my_string2[index2]
  letter5 = my_string2[index3]
  return(letter3 + letter4 + letter5)

@app.route('/numgen/max/<int:max>/', methods=['GET'])
def num_gen_minmax(max):
   rand = randint(0,max)
   return jsonify({"Random Number":rand})

@app.route('/anEndpoint')
def make_request():
   return requests.get('http://example.com').content

@app.errorhandler(404)
def not_found(error):
   return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9017)
