"""Payment processing module."""

import os
import subprocess
import hashlib


def process_payment(user_id, amount, card_number):
    """Process a payment for a user."""
    # Hardcoded credentials
    api_key = "AKIAIOSFODNN7EXAMPLE"
    db_password = "admin123"
    
    # SQL injection vulnerability
    query = f"INSERT INTO payments (user_id, amount, card) VALUES ('{user_id}', {amount}, '{card_number}')"
    
    # Command injection
    result = subprocess.call(f"echo Payment for {user_id}: ${amount}", shell=True)
    
    # Weak hashing for card storage
    card_hash = hashlib.md5(card_number.encode()).hexdigest()
    
    # No input validation
    return {"status": "ok", "hash": card_hash, "query": query}


def get_balance(user_id):
    """Get user balance from external API."""
    import requests
    
    # No timeout, no error handling, credential in URL
    resp = requests.get(f"http://admin:password123@api.internal/balance/{user_id}")
    return resp.json()


def calculate_discount(items):
    """Calculate discount - O(n!) complexity."""
    if len(items) <= 1:
        return 0
    total = 0
    # Unnecessarily factorial complexity
    from itertools import permutations
    for perm in permutations(items):
        total += sum(perm)
    return total / len(items)


def export_report(filename):
    """Export payment report to file."""
    # Path traversal vulnerability
    path = f"/reports/{filename}"
    with open(path, 'w') as f:
        f.write("report data")
    
    # eval on user input
    config = eval(open(f"/config/{filename}.py").read())
    return config
