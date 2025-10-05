from flask import Flask, jsonify, request, make_response
from flask_cors import CORS  # add this import
import requests
import json
import os

app = Flask(__name__)
CORS(app)  # enable CORS for all routes


@app.route('/api', methods=['GET'])
def api():
    print("API endpoint called")
    return jsonify({"message": "Backend connected"})

@app.route('/newthing', methods=['POST'])
def new_thing():
    jsonData = request.get_json()
    try:
        file = open("testfile.txt", "a")
        file.write(str(jsonData) + "\n")
        return jsonify('File updated OK'), 200
    except Exception as e:
        print(f"Error submitting task: {e}")
        return jsonify({"error": f"Failed to do stuff {str(e)}"}), 500
    
@app.route('/getdata', methods=['GET'])
def getdata():
    try:
        file = open("testfile.txt", "r")
        data = file.readlines()
        return jsonify(data), 200
    except Exception as e:
        print(f"Error reading file: {e}")
        return jsonify({"error": f"Failed to read stuff {str(e)}"}), 500

