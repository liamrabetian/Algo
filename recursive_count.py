#### T: O(n), S: O(n)


def count(arr):
    if len(arr) == 0:
        return 0
    arr.pop()
    return 1 + count(arr)


if __name__ == "__main__":
    arr = [2, 1, 5, 4, 4, 7]
    print(count(arr))
