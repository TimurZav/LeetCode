# Python3 program to find the length
# of the longest substring without
# repeating characters

# This function returns true if all
# characters in str[i..j] are
# distinct, otherwise returns false
def are_distinct(row, i, j):
    # Note : Default values in visited are false
    visited = [0] * 26

    for k in range(i, j + 1):
        if visited[ord(row[k]) - ord('a')]:
            return False

        visited[ord(row[k]) - ord('a')] = True

    return True


# Returns length of the longest substring
# with all distinct characters.
def longest_unique_substtr(row):
    n = len(row)

    # Result
    res = 0

    for i in range(n):
        for j in range(i, n):
            if are_distinct(row, i, j):
                res = max(res, j - i + 1)

    return res


# Driver code
if __name__ == '__main__':
    string = "dvdf"
    print("The input is ", string)

    length = longest_unique_substtr(string)
    print("The length of the longest non-repeating character substring is ", length)
