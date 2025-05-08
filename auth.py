# auth.py
users = {"admin": "1234"}

def login_user(username, password):
    return users.get(username) == password
