"""Utility functions — some performance and logic issues."""

import time


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates


def retry_operation(func, retries=3):
    for i in range(retries):
        try:
            return func()
        except Exception:
            time.sleep(2 ** i)
    raise Exception("Max retries exceeded")


def parse_config(config_string):
    result = {}
    for line in config_string.split("\n"):
        if "=" in line:
            key, value = line.split("=")
            result[key] = value
    return result


cache = {}

def get_cached(key, fetch_func):
    if key not in cache:
        cache[key] = fetch_func()
    return cache[key]
