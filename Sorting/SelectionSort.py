# Time complexity O(N^2) and Space complexity O(1)


array = [4,2,3,5,8,5,7,95,34]

def selectionSort(array):
    currentIdx = 0 # Starting index
    while currentIdx < len(array) -1:  # You want to iterate till the length of the array
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:  # To move the pointer to next idx
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

    
    
print(selectionSort(array))
