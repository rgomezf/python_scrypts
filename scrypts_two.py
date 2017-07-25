# Anti Vowel function
def anti_vowel(text):
    new_text = ""
    for n in range(0, len(text)):
        if text[n] not in "aeiouAEIOU":
            new_text += text[n]
    return new_text

if __name__ == '__main__':
    assert anti_vowel("ramon") == "rmn", "Should return 'rmn'"
    assert anti_vowel("Antiterrorism") == "nttrrrsm"
    assert anti_vowel("Abba") == "bb"
    
# Scrabble Score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    new_word = word.lower()
    total = 0
    for n in new_word:
        total += score[n]
    return total

if __name__ == '__main__':
    assert scrabble_score("ramon") == 7
    assert scrabble_score("python") == 14

# Censor, replace a word on a string with '*' of the lenght of the word
def censor(text, word):
    list = text.split()
    asterisk = len(word) * "*"
    
    for item in range(len(list)):
        if list[item] == word:
            list[item] = asterisk
    return " ".join(list)

if __name__ == '__main__':
    assert censor("hey hey hey", "hey") == "*** *** ***"
    assert censor("this hack is wack hack", "hack") == "this **** is wack ****"
