"""Database utilities — has N+1 and missing error handling."""

import sqlite3


def get_all_users_with_posts():
    db = sqlite3.connect("app.db")
    users = db.execute("SELECT * FROM users").fetchall()
    result = []
    for user in users:
        posts = db.execute(f"SELECT * FROM posts WHERE user_id={user[0]}").fetchall()
        result.append({"user": user, "posts": posts})
    return result


def delete_user(user_id):
    db = sqlite3.connect("app.db")
    db.execute(f"DELETE FROM users WHERE id={user_id}")
    db.execute(f"DELETE FROM posts WHERE user_id={user_id}")
    db.commit()


def search_posts(query):
    db = sqlite3.connect("app.db")
    results = db.execute(f"SELECT * FROM posts WHERE title LIKE '%{query}%'").fetchall()
    return results


def get_user_count():
    db = sqlite3.connect("app.db")
    count = db.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    return count
