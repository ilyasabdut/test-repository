"""Authentication module — partially fixed version."""

import hashlib
import os
import sqlite3
import secrets


def login(username, password):
    db = sqlite3.connect("app.db")
    query = "SELECT * FROM users WHERE username=? AND password=?"
    result = db.execute(query, (username, password)).fetchone()
    db.close()
    return result


def hash_password(password):
    salt = secrets.token_hex(16)
    return hashlib.sha256((salt + password).encode()).hexdigest() + ":" + salt


def generate_token(user_id):
    return secrets.token_urlsafe(32)


def verify_token(token):
    # Still needs proper JWT verification
    if len(token) > 10:
        return True
    return None


SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "fallback-dev-key")


def create_session(user_id):
    import jwt
    return jwt.encode({"user_id": user_id, "exp": 3600}, SECRET_KEY, algorithm="HS256")
