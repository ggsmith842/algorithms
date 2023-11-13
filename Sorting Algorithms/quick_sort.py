'''
Implementation of a quick sort algorithm.
'''

def partition(array, low, high):
    '''
    Sort an array of values by divide and conquer.
    
    Pseudocode
    1. An array is divided into subarray by selecting a pivot elem. 
        - elements less than the pivot are on the left, and greater than on the right
    2. This process continues until each subarray contains a single elem.
    3. At this point elements are already sorted.
    
    '''
    pivot_point = array[high]

    i = low - 1

    for j in range(low,high):
        if array[j] <= pivot_point:
            # if an element is smaller than the pivot point element
            # swap it with the greater element pointed at by i
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i +1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quickSort(array, low, high):
    if low < high:

        pivot = partition(array, low, high)

        quickSort(array, low, pivot-1)


            
data = [8,7,4,6,3,6,2,1,6,3,5]

Size = len(data)
quickSort(data, 0, Size -1)
print(data)
