#### T: O(n) S: O(n)


def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


if __name__ == "__main__":
    x = 5
    print(fact(5))
