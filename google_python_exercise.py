# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
def match_ends(words):
    new_words = [p for p in words if len(p) >= 2]
    count = 0
    for n in new_words:
        if n[0] == n[-1]:
            count += 1
    return count

if __name__ == '__main__':
    assert match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']) == 3, "Solution correct, they're 3"
    assert match_ends(['', 'x', 'xy', 'xyx', 'xx']) == 2, "Only 2"
    assert match_ends(['aaa', 'be', 'abc', 'hello']) == 1, "Just 1"
    
    
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
def front_x(words):
    first_list = [word for word in words if word[0] == 'x']
    second_list = [word for word in words if word[0] != 'x']

    return sorted(first_list) + sorted(second_list)

if __name__ == '__main__':
    assert front_x(['xaa', 'xzz', 'axx', 'bbb', 'ccc']) == ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    assert front_x(['xaa', 'xcc', 'aaa', 'bbb', 'ccc']) == ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    assert front_x(['xanadu', 'xyz', 'aardvark', 'apple', 'mix']) == ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
