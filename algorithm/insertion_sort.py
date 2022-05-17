def insertion_sort(input_list):
    total_length = len(input_list)
    if total_length == 1:
        return input_list

    sortable_index = 1
    while total_length > sortable_index:
        sortable_element = input_list[sortable_index]
        i = sortable_index - 1
        while i >= 0 and sortable_element < input_list[i]:
            input_list[i + 1] = input_list[i]
            i = i - 1
        input_list[i + 1] = sortable_element
        sortable_index = sortable_index + 1
    return input_list


if __name__ == "__main__":
    assert insertion_sort([1, 6, 4, 7, 2, 9]) == [1, 2, 4, 6, 7, 9]
