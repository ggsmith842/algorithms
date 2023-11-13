'''
Binary search implementation.
'''

def binary_search(array, subject, low, high):
    '''
    Seaches an array for a subject and 
    return the position of the suject if found.

    Implemented using recursive method.
    '''

    if low > high:
        return "No value found in data."
    else:
        mid = low + (high - low) // 2

        if subject == array[mid]:
            return f'Value {subject} found at {mid}'
        elif subject > array[mid]:
            return binary_search(array, subject, mid + 1, high)
        else:
            return binary_search(array, subject, low, mid - 1)


data = [10,11,12,13,14,15]

print(binary_search(data, 13,0, len(data)-1))