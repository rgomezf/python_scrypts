def find_message(text):
    """Find a secret message"""
    message = ""
    for n in range(0, len(text)):
        if text[n].isupper():
            message += text[n]
    return message

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    assert find_message("A") == "A", "Letter A"
