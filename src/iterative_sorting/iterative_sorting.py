# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # for i in range index[0] to length of arr minus 1
    for i in range(0, len(arr) - 1):
        # assume i is smallest value to start
        lowest = i
        # j starts at i + 1 so you compare i to j
        for j in range(i + 1, len(arr)):
            # if arr[j] is smaller than arr[i], make j smallest index
            if arr[j] < arr[lowest]:
                lowest = j
        # if i is not lowest, swap the values
        if i != lowest:
            arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr


print(selection_sort([3, 1, 5, 6, 4, 7, 2]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
