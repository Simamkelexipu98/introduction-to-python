import pytest

from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_value_h():
    assert value("hi") == 20
    assert value("Hey there") == 20
    assert value("H") == 20

def test_value_other():
    assert value("Goodbye") == 100
    assert value("what's up") == 100
    assert value("bye") == 100

