"""
    One Away Strings (Python)

    Write a function that takes two strings and returns True if they are one away from each other.

    They are one away from each other if a single operation (changing a character, deleting a character or adding a character) will change one of the strings to the other.

    Examples:

    "abcde" and "abcd" are one away (deleting a character).
    "a" and "a" are one away (changing the only character 'a' to the equivalent character 'a').
    "abc" and "bcc" are NOT one away. (They are two operations away.)
"""

# Implement your function below.
def is_one_away(s1, s2):
    return False

# NOTE: The following input values will be used for testing your solution.
is_one_away("abcde", "abcd")  # should return True
is_one_away("abde", "abcde")  # should return True
is_one_away("a", "a")  # should return True
is_one_away("abcdef", "abqdef")  # should return True
is_one_away("abcdef", "abccef")  # should return True
is_one_away("abcdef", "abcde")  # should return True
is_one_away("aaa", "abc")  # should return False
is_one_away("abcde", "abc")  # should return False
is_one_away("abc", "abcde")  # should return False
is_one_away("abc", "bcc")  # should return False
