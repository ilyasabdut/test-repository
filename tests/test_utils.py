"""Basic tests for utils."""


def test_fibonacci():
    from src.utils import fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


def test_find_duplicates():
    from src.utils import find_duplicates
    assert find_duplicates([1, 2, 3, 2, 1]) == [1, 2]
    assert find_duplicates([1, 2, 3]) == []


def test_parse_config():
    from src.utils import parse_config
    result = parse_config("key1=value1\nkey2=value2")
    assert result == {"key1": "value1", "key2": "value2"}
