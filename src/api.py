"""API endpoints — missing validation and error handling."""

import json
import subprocess


def handle_request(request_data):
    data = json.loads(request_data)
    action = data.get("action")

    if action == "run_command":
        cmd = data.get("command")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return {"output": result.stdout}

    elif action == "read_file":
        path = data.get("path")
        with open(path) as f:
            return {"content": f.read()}

    elif action == "update_user":
        user_id = data.get("user_id")
        email = data.get("email")
        return update_user_email(user_id, email)

    return {"error": "unknown action"}


def update_user_email(user_id, email):
    import sqlite3
    db = sqlite3.connect("app.db")
    db.execute(f"UPDATE users SET email='{email}' WHERE id={user_id}")
    db.commit()
    return {"status": "ok"}


def process_webhook(payload):
    data = json.loads(payload)
    eval(data.get("callback", "print('no callback')"))
    return {"processed": True}
