import random


def rooster_sort(unsorted_list: list) -> list:
    result = unsorted_list.copy()
    roosters_corner = list()

    # part 1: stalin's sort
    i = 1
    while i < len(result):
        prev_elem = result[i - 1]
        current_elem = result[i]
        if current_elem >= prev_elem:
            i += 1
        else:
            result.pop(i)
            roosters_corner.append(current_elem)

    # part 2: sorting roosters
    if len(roosters_corner) > 1:
        roosters_corner = rooster_sort(roosters_corner)

    # part 3: inserting roosters back
    i = 0
    while i < len(result) and len(roosters_corner) > 0:
        straight_elem = result[i]
        rooster = roosters_corner[0]
        if rooster < straight_elem:
            roosters_corner.pop(0)
            result.insert(i, rooster)
        else:
            i += 1

    if len(roosters_corner):
        print("result list", result)
        print("rooster's corner", roosters_corner)
        raise ValueError("Something wrong with sorting")

    return result


if __name__ == '__main__':
    sample_list = list()
    LIST_LENGTH = 20
    MIN_VALUE = -100
    MAX_VALUE = 100
    for i in range(LIST_LENGTH):
        sample_list.append(random.randint(MIN_VALUE, MAX_VALUE))
    print(sample_list)
    sorted_list = rooster_sort(sample_list)
    print(sorted_list)
