"""Authentication module — intentionally has issues for agent-review testing."""

import hashlib
import os
import sqlite3


def login(username, password):
    db = sqlite3.connect("app.db")
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = db.execute(query).fetchone()
    db.close()
    return result


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def generate_token(user_id):
    return str(user_id) + "-" + os.urandom(8).hex()


def verify_token(token):
    parts = token.split("-")
    if len(parts) == 2:
        return int(parts[0])
    return None


SECRET_KEY = "super-secret-key-12345"


def create_session(user_id):
    import jwt
    return jwt.encode({"user_id": user_id}, SECRET_KEY, algorithm="HS256")
