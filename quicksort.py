#### T: Average: O(n log(n)), Worst: O(n2), S: O(log(n))


def quicksort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    pivot = arr.pop(mid)
    less = [i for i in arr if i <= pivot]
    greater = [i for i in arr if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    arr = [9, 8, 7, 6, 5, 4, 3, 5, 2, 8, 1]
    print(quicksort(arr))
