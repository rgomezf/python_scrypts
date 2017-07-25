# Function that takes an integer as input
# and calculate and return the factorial of that number

def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)

if __name__ == '__main__':
    #These "asserts" using only for self-checking
    assert factorial(4) == 24, "Would equal 24"
    assert factorial(1) == 1, "Would equal 1"
    assert factorial(3) == 6, "Would equal 6"
    assert factorial(0) == 1, "Would equal 1"

def is_prime(x):
    if x < 2:
        return False
    for n in range(2, x-1):
        if x % n == 0:
            return False
    else:
        return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking
    assert is_prime(4)  == False, "Would equal False"
    assert is_prime(21) == False, "Would equal False"
    assert is_prime(11) == True, "Would equal True"
    assert is_prime(18) == False, "Would equal False"
    assert is_prime(0)  == False
    assert is_prime(1)  == False
    
