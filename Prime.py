import math

def isPrime(number):
    if number%2 == 0:
        return False
    if number <= 1:
        return False
    if number <= 3:
        return True
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def test_small_2():
    assert isPrime(2) == False

def test_small_3():
    assert isPrime(3) == True

def test_small_21():
    assert isPrime(21) == False
