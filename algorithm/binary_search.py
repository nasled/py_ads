def binary_search(input_list, needle_value):
    input_length = len(input_list)
    left_index = 0
    right_index = input_length - 1
    while right_index >= left_index:
        center_index = (left_index + right_index) // 2
        if needle_value > input_list[center_index]:
            left_index = center_index + 1
        elif input_list[center_index] > needle_value:
            right_index = center_index - 1
        else:
            return center_index
    return -1


def binary_search_alt(input_list, needle_value):
    input_length = len(input_list)
    left_index = 0
    right_index = input_length - 1
    while left_index is not right_index:
        center_index = -(-(left_index + right_index) // 2)
        if input_list[center_index] > needle_value:
            right_index = center_index - 1
        else:
            left_index = center_index
    if input_list[left_index] is needle_value:
        return left_index
    return -1


if __name__ == "__main__":
    source_list = [1, 3, 5, 7, 10, 13, 15]

    assert binary_search(source_list, -1) == -1
    assert binary_search(source_list, 999) == -1
    for index, value in enumerate(source_list):
        assert binary_search(source_list, value) == index

    assert binary_search_alt(source_list, -1) == -1
    assert binary_search_alt(source_list, 999) == -1
    for index, value in enumerate(source_list):
        assert binary_search_alt(source_list, value) == index
