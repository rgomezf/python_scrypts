# Count function.  Receive two parameters
# returns the occurrences of one in the other
def count(sequence, item):
    found = 0
    for n in sequence:
        if n == item:
            found += 1
    return found

if __name__ == '__main__':
    assert count([1,2,1,1], 1) == 3

# Purify.  Remove the odd numbers from a list
def purify(numbers):
    new_list = []
    for item in numbers:
        if item % 2 == 0:
            new_list.append(item)
    return new_list

if __name__ == '__main__':
    assert purify([1,2,3]) == [2]
    assert purify([4,5,5,4]) == [4, 4]

# Remove duplicates.  Removes elements of the list that are the same.
def remove_duplicates(numbers):
    new_list = []
    for n in numbers:
        if n not in new_list:
            new_list.append(n)
    return new_list

if __name__ == '__main__':
    assert remove_duplicates([1,1,2,2,1,2,1,2]) == [1, 2]

# Median.  takes a list as an input and returns the median value of the list.
from math import floor
def median(numbers):
    sorted_list = sorted(numbers)
    list_len = floor(len(numbers) / 2)
   
    if sorted_list[list_len] % 2 == 0:
        return sorted_list[list_len]
    else:
        return (sorted_list[list_len-1] + sorted_list[list_len]) \
               / 2.0 if list_len > 1 else sorted_list[list_len]

if __name__ == '__main__':    
    assert median([5,2,3,1,4]) == 2.5
    assert median([7,12,3,1,6]) == 6
    assert median([1]) == 1
    
    
