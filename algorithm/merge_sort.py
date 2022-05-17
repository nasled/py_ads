def merge_ordered(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while len(left) > 0:
        result.append(left.pop(0))
    while len(right) > 0:
        result.append(right.pop(0))
    return result


def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list

    middle = int(round(len(input_list) / 2))
    left = merge_sort(input_list[:middle])
    right = merge_sort(input_list[middle:])

    return merge_ordered(left, right)


if __name__ == "__main__":
    assert merge_sort([1, 6, 4, 7, 2, 9]) == [1, 2, 4, 6, 7, 9]
