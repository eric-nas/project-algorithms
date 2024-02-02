def is_anagram(first_string, second_string):
    first_string_low = first_string.lower()
    second_string_low = second_string.lower()
    list_first_string = list(first_string_low)
    list_second_string = list(second_string_low)

    for x in range(len(list_first_string) - 1):
        min = x

        for y in range(x + 1, len(list_first_string)):
            if list_first_string[y] < list_first_string[min]:
                min = y
        current_element = list_first_string[x]
        list_first_string[x] = list_first_string[min]
        list_first_string[min] = current_element
    
    string_order1 = ''.join(list_first_string).lower()

    for x in range(len(list_second_string) - 1):
        min = x

        for y in range(x + 1, len(list_second_string)):
            if list_second_string[y] < list_second_string[min]:
                min = y
        current_element = list_second_string[x]
        list_second_string[x] = list_second_string[min]
        list_second_string[min] = current_element

    string_order2 = ''. join(list_second_string).lower()

    return (string_order1, string_order2, string_order1 == string_order2)

is_anagram('muro', 'RuMo')
