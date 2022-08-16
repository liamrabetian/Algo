#### T: O(n), S: O(1)

# 1 <= n < 1000
# if i % 3 --> Fizz
# if i % 5 --> Buzz
# if i % 3 & 5 --> FizzBuzz
# else --> "i"


# naive way ? describe
# string concatinating way? describe

# third way which is optimization of the string concatinating way with HashTable


def fizz_buzz(n):
    fizz_buzz_map = {3: "Fizz", 5: "Buzz", 7: "Jazz"}
    divisors = [3, 5, 7]
    output_arr = []

    for i in range(1, n + 1):
        ans_str = ""
        for key in divisors:
            if i % key == 0:
                ans_str += fizz_buzz_map[key]
        if not ans_str:
            ans_str = str(i)
        output_arr.append(ans_str)
    return output_arr


if __name__ == "__main__":
    n = 100
    print(fizz_buzz(n))
