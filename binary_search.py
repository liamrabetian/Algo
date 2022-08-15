### T: O(log(n)) S: O(1)


def binary_search(l, item):
    if not l:
        return None

    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == item:
            return mid
        elif l[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    l = [1, 3, 4, 5, 7]
    item = 5
    print(binary_search(l, item=item))
