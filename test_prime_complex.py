from Prime import isPrime
import time

def test_small_0():
    assert isPrime(0) == False

def test_small_1():
    assert isPrime(1) == False

def test_small_negative():
    assert isPrime(-7) == False

def test_small_21():
    assert isPrime(21) == False

def test_small_big():
    assert isPrime(87178291199) == True

def test_small_big_false():
    assert isPrime(87178291197) == False



