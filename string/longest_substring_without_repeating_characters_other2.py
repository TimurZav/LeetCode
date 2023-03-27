
def longest_unique_substtr(s):
    char_set = set()
    max_len, start = 0, 0
    for i, c in enumerate(s):
        while c in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(c)
        max_len = max(max_len, i - start + 1)
    return max_len


# Driver code
if __name__ == '__main__':
    string = "adsvdf"
    print("The input is ", string)

    length = longest_unique_substtr(string)
    print("The length of the longest non-repeating character substring is ", length)
