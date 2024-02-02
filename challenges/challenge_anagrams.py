def merge_sort(numbers, start=0, end=None):
    """Faça o código aqui."""
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)
    return numbers


def merge(numbers, start, mid, end):
    """Faça o código aqui."""
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    """Faça o código aqui."""

    first_word = first_string.lower()
    second_word = second_string.lower()

    first_new_word = "".join(merge_sort(list(first_word)))
    second_new_word = "".join(merge_sort(list(second_word)))

    if first_string == "" and second_string == "":
        return (first_new_word, second_new_word, False)

    return (first_new_word, second_new_word, first_new_word == second_new_word)
