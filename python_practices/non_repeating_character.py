"""
    Non-Repeating Character
    Implement a function that takes a string and returns the first character that does not appear twice or more.
    Example:
        "abacc" -> 'b' ('a' appears twice, and so does 'c')
        "xxyzx" -> 'y' ('y' and 'z' are non-repeating characters, and 'y' appears first)
        If there is no non-repeating character, return None.
"""

def non_repeating(given_string):
    """
        Go through each character in the string and map them to a dictionary
        where the key is the character and the value is the time that character appear
        in the string.

        Because the dictionary doesn't store thing in order. Therefore, we cannot loop
        through the dictionary and check if the value equal to 1 then return because
        there will be a case that it's not the order that we put in. (maybe the last one,
        but we expect the first one)

        So we have 2 options:
            1. Use another data structure, stack, to track back
            2. Simply loop through the given string again and return if that character count
            is 1. This time, it always the first one.
    """
    char_count = {}

    for char in given_string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    for char in given_string:
        if char_count[char] == 1:
            return char

    return None


if __name__ == '__main__':
    print(non_repeating("abcab"))   # 'c'
    print(non_repeating("abab"))    # None
    print(non_repeating("aabbbc"))  # 'c'
    print(non_repeating("aabbdbc")) # 'd'