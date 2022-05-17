def bubble_swap(x, y):
    cur = x
    x = y
    y = cur
    return [x, y]


def bubble_sort(input_list):
    total_length = len(input_list)
    if total_length == 1:
        return input_list

    for outer_index in range(total_length):
        for inner_index in range(total_length - outer_index - 1):
            if input_list[inner_index] > input_list[inner_index + 1]:
                input_list[inner_index], input_list[inner_index + 1] =\
                    bubble_swap(input_list[inner_index], input_list[inner_index + 1])
    return input_list


def bubble_sort_greedy(input_list):
    total_length = len(input_list)
    if total_length == 1:
        return input_list

    for outer_index in range(0, len(input_list)-1):
        for inner_index in range(0, len(input_list) - 1):
            if input_list[outer_index] < input_list[inner_index]:
                input_list[inner_index], input_list[outer_index] =\
                    bubble_swap(input_list[inner_index], input_list[outer_index])
    return input_list


if __name__ == "__main__":
    assert bubble_sort([1, 6, 4, 7, 2, 9]) == [1, 2, 4, 6, 7, 9]
    assert bubble_sort_greedy([1, 6, 4, 7, 2, 9]) == [1, 2, 4, 6, 7, 9]
