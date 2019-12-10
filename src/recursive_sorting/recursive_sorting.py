# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # start with empty array that will be appended to
    arrC = []
    # starting indexes
    a_index = 0
    b_index = 0
    # while the index is less than the length off the arr, do the rest
    while a_index < len(arrA) and b_index < len(arrB):
      # if arrA at an index is less than arrB at an index, append it to arrC and move the index +1
        if arrA[a_index] < arrB[b_index]:
            arrC.append(arrA[a_index])
            a_index += 1
      # else do the opposite of above
        else:
            arrC.append(arrB[b_index])
            b_index += 1
    # since when we compared the nums between arrA and arrB, the higher num will be left off at the end.
    # therefore, if the length of arrA is equal to its current index, you append arrB at b_index because it has 1 more item.
    if a_index == len(arrA):
        arrC.extend(arrB[b_index:])
    # else do the opposite of above
    else:
        arrC.extend(arrA[a_index:])
    return arrC


print(merge([1, 3, 5], [2, 4, 6]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # split the list into 2 lists and call merge_sort function recursively
    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])

    # call the helper function from above to merge left and right
    return merge(left, right)


print(merge_sort([12, 13, 11, 14, 9, 100, 3, 2, 17, 19, 201]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
