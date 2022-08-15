### O(n2)


def find_smallest_index(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        index = find_smallest_index(arr)
        new_arr.append(arr.pop(index))
    return new_arr


if __name__ == "__main__":
    arr = [2, 1, 5, 4, 7, 9, 8, 3]
    print(selection_sort(arr=arr))
