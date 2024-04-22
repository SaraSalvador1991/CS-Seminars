#1. Bubble Sort: epeatedly iterates through the list,
# comparing adjacent elements and swapping them if they are in the wrong order.
def bubble_sort(arr):  # complexity O(n^2) - worst case, O(n) - best case
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]: # if this holds
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap arr[j] and arr[j+1]


# 2. Selection Sort: divides the input list into two parts: a sorted sublist at the beginning
# and an unsorted sublist at the end.
# It repeatedly finds the smallest element in the unsorted sublist and swaps it with the first unsorted element,
# thus gradually expanding the sorted sublist until the entire list is sorted.
def selection_sort(arr):   #Time Complexity: O(n^2) in all cases.
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]: # of this holds
                min_idx = j # update min_idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # arrange the array


# 3. Insertion Sort: builds the final sorted array one element at a time.
# It works by iteratively taking one element from the unsorted part of the array
# and inserting it into its correct position in the sorted part of the array.
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted
        j = i - 1     # Index of the last element in the sorted sublist

        # Move elements of arr[0,..,i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct position in the sorted sublist
        arr[j + 1] = key

# 4. Merge sort: It works recursively by dividing the array into two halves,
# sorting each half separately, and then merging the sorted halves into a single sorted list.
# The time complexity of Merge Sort is
# O(n*logn) in both the average and worst cases, making it efficient for large datasets.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # find the middle point of the array (floor division)
        left_half = arr[:mid]  # divide the array in half
        right_half = arr[mid:]

        merge_sort(left_half)  # ricorsive ordering for the first half
        merge_sort(right_half)  # ricorsive ordering for the second half

        # merge the two half
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements, if any, from left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # same for the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Esempio di utilizzo:
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Array ordinato:", arr)


