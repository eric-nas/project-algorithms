def is_palindrome_iterative(word):
    if word == '':
        return False
    reversedWord = ''.join(reversed(word))
    if word == reversedWord:
        return True
    return False
