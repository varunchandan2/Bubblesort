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

 # This is the most effective iterative method using pointers 
 # Time complexity is O(n) | Space comlexity is O(1)
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True
            

print(isPalindrome(string))