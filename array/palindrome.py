import itertools


dict_palindrome: dict = {
    "one_multiplier": 0,
    "two_multiplier": 0,
    "multiplied": 0,
}

for one_multiplier, two_multiplier in itertools.product(range(900, 1000), range(900, 1000)):
    multiplied_digit: int = one_multiplier * two_multiplier
    str_multiplied_digit: str = str(multiplied_digit)
    str_multiplied_digit_reversed: str = str_multiplied_digit[::-1]
    if str_multiplied_digit == str_multiplied_digit_reversed \
            and multiplied_digit > dict_palindrome["multiplied"]:
        maximum = int(str_multiplied_digit)
        dict_palindrome["one_multiplier"] = one_multiplier
        dict_palindrome["two_multiplier"] = two_multiplier
        dict_palindrome["multiplied"] = multiplied_digit


print(dict_palindrome)
