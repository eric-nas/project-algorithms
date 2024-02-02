def is_palindrome_recursive(word, low_index, high_index):
    if word == '':
        return False
    if len(word) == 1:
        return True
    letter1 = word[high_index]
    letter2 = word[low_index]
    if letter1 == letter2 and word[1:-1] == '':
        return True
    if letter1 == letter2:
        return is_palindrome_recursive(word[1:-1], 0, -1)
    return False
