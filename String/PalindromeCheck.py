string = 'abcdcba'


# Solving iteratively by creating a new string and checking of both string matches
# Time complexity is O(n^2) | Space comlexity is O(n)

def palindromeCheck(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString

print(palindromeCheck(string))