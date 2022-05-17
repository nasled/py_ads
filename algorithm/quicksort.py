def quicksort(arr):
    if not arr:
        return []

    pivots = [x for x in arr if x == arr[0]]
    lesser = quicksort([x for x in arr if x < arr[0]])
    greater = quicksort([x for x in arr if x > arr[0]])

    return lesser + pivots + greater


if __name__ == "__main__":
    assert quicksort([3, 1, 3, 4, 5, 1, 0]) == [0, 1, 1, 3, 3, 4, 5]
