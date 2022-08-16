#### T: O(n), S: O(n)


def sum(arr):
    if len(arr) == 0:
        return 0
    return arr.pop() + sum(arr)


if __name__ == "__main__":
    arr = [2, 1, 5]
    print(sum(arr))
