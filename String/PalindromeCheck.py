string = 'abcdcba'


# Solving iteratively by creating a new string and checking of both string matches
# Time complexity is O(n^2) | Space comlexity is O(n)

def palindromeCheck1(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString

print(palindromeCheck1(string))


# Solving iteratively with array which improves the time complexity 
# Time complexity is O(n) | Space comlexity is O(n)

def palindromeCheck2(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)

print(palindromeCheck2(string))