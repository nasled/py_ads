def union(set1, set2):
    union_set = set()
    for set1_index in range(len(set1)):
        union_set.add(set1.pop())
    for set2_index in range(len(set2)):
        union_set.add(set2.pop())
    return union_set


def intersection(set1, set2):
    if len(set1) > len(set2):
        smaller_set = set2
    else:
        smaller_set = set1
    intersection_set = set()
    for set_index in range(len(smaller_set)):
        if smaller_set[set_index] in set1 and smaller_set[set_index] in set2:
            intersection_set.add(smaller_set[set_index])
    return intersection_set


if __name__ == "__main__":
    assert union({1, 2, 3}, {4, 5}) == {1, 2, 3, 4, 5}
    assert {1, 2, 3}.union([4, 5]) == {1, 2, 3, 4, 5}
    assert intersection([1, 2, 3], [1, 2, 4]) == {1, 2}
    assert {1, 2, 3}.intersection([1, 2, 4]) == {1, 2}
