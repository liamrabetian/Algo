### roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
### sample input = "MCMXCIV"
### T: O(1), S: O(1)


def roman_to_int(s: str) -> int:
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    i = 0  # number of steps to take
    while i < len(s):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            result += roman_map[s[i + 1]] - roman_map[s[i]]
            i += 2
        else:
            result += roman_map[s[i]]
            i += 1
    return result


if __name__ == "__main__":
    roman_number = "MCMXCIV"
    print(roman_to_int(roman_number))
