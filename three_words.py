# check if the string contains three words in succession. 
# For example, the string "start 5 one two three 7 end" contains three words in succession.

def three_words(words):
    new_list = words.split()
    counter = 0
    for n in new_list:
        if n.isnumeric() == True:
            counter = 0
        elif counter == 3:
            break
        counter += 1
  
    if counter == 3:
        return True
    else:
        return False
    
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"

# Absolute Sorting
# he list or tuple (but not a generator) sorted by absolute values in ascending order.

def checkio(numbers_array):

    list_numbers = []
    for elem in numbers_array:
        list_numbers.append(elem)
    list_numbers = sorted(list_numbers, key=lambda number: abs(number))

    return list_numbers

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
