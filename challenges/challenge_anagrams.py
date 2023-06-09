def sort_string(string):
    string_list = list(string)

    for index in range(1, len(string_list)):
        key = string_list[index]
        j = index - 1
        while j >= 0 and string_list[j] > key:
            string_list[j + 1] = string_list[j]
            j -= 1
        string_list[j + 1] = key
    return "".join(string_list)


def is_anagram(first_string, second_string):
    first_string_sorted = sort_string(first_string.lower())
    second_string_sorted = sort_string(second_string.lower())
    if not first_string_sorted or not second_string_sorted:
        return first_string_sorted, second_string_sorted, False
    elif first_string_sorted == second_string_sorted:
        return first_string_sorted, second_string_sorted, True
    else:
        return first_string_sorted, second_string_sorted, False
