array = [2,7,4,52,55,6,63,65,2,54]

def insertionSort(array):
    for i in range(1, len(array)):  # We will be looking from index 1 to length of array
        j = i                       # Now j is the part of our tentative sorted array and will do comparison on j
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1

    return array






def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(insertionSort(array))
