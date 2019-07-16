# TO-DO: Complete the selection_sort() function below 
test = [1, 5, 6, 7, 9, 10, 3, 4, 2, 8]
test2 = [1, 5, 6, 7, 9, 10, 3, 4, 2, 8]
def selection_sort( arr ):
    # loop through n-1 elements except last index
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        #loop though each index in array
        for each_index in range(cur_index, len(arr)):

        #if item at index is smaller than beginning of array set it there
            if arr[each_index] < arr[smallest_index]:
                    smallest_index = each_index 

        #set temp to hold item at smallest index
        temp = arr[smallest_index]
        #set smallest index to current index
        arr[smallest_index] = arr[cur_index]

        arr[cur_index] = temp




    return arr

print(selection_sort(test))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    #keep track of swapping
    swap = True

    while swap:

        swap = False

        for i in range(0, len(arr) - 1):

            #cur_index = i (not needed?)

            if arr[i] > arr [i + 1]:
                #swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                #set to true if swap happened
                swap = True

    return arr

print(bubble_sort(test2))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr