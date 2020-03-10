from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/api/users')
def api_users():
    users = get_users()
    if not users:
        return 'There are no users defined'
    return jsonify(users)

@app.route('/api/users/add/<username>')
def api_users_add(username):
    users = get_users()
    if username in users:
        return '{} already in users'.format(username)
    users.append(username)
    write_users(users)
    return '{} added to users'.format(username)


def get_users():
    with open('users.json', 'r') as f:
        return json.load(f)

def write_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f)