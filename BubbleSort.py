# Find the 2nd Highest number in the list
# Time complexity O(n^2) for worst case and O(n) for the best case
# Space complexity = 0(1) because we are not creating any additional space


list = [0,12,34,52,4,64,56]
 

def secondHighestNumber(list):
    isSorted = False                                # Assume the variable is not sorted
    counter = 0                                     # Using counter to keep track of iterations
    while not isSorted:                             # Using while loopWhile this array is not sorted
        isSorted = True                             # let say for instance it is sorted then applying for loop
        for i in range(len(list) - 1 - counter):    # Leaving the last element 
            if list[i] > list[i+1]:                 # Using the bubble sort algorithm with checking the adjacent elements and swapping
                swap(i, i + 1, list)
                isSorted = False
        counter += 1                                
    return list[-2]



# Swap helper method  
def swap(i, j, list):
    list[i], list[j] = list[j], list[i]


# Print the 2nd highest number
print(secondHighestNumber(list))