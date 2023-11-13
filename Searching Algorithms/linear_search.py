'''
Example of a linear sort. 

Applications: Used when an array size is <100 elements.
'''

unsorted_list = [2,None,0,1,9]

def linear_search(array, subject):
    '''
    Perform a linear search on an array of values. 
    '''
    for idx, element in enumerate(array):
        if element == subject:
            return "Element found at  " + str(idx)
        
    return "Element not found."

if __name__=='__main__':

    print(linear_search(unsorted_list, 9))