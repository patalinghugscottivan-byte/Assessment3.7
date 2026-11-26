

FULL_NAME = "Scott Ivan Patalinghug"


def build_unsorted_array(name):

    letters = [ch for ch in name.upper() if ch.isalpha()]
    result = []
    for ch in letters:
        if letters.count(ch) == 1:
            result.append(ch)
    return result


def insertion_sort(arr):

    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


if __name__ == "__main__":
    unsorted_array = build_unsorted_array(FULL_NAME)
    sorted_array = insertion_sort(unsorted_array)

    print("Full name      :", FULL_NAME)
    print("Unsorted array :", unsorted_array)
    print("Sorted array   :", sorted_array)