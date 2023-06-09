def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    if type(low_index) != int and type(high_index) != int:
        low_index = 0
        high_index = len(word) - 1

    if word[low_index] != word[high_index]:
        return False

    if low_index + 1 >= high_index - 1:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
