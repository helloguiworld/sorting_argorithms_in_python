from swap import swap

# Ensures that the root of a max-heap is the largest number among it and its children
def heapify(array, root, limit = -1):
    if(limit == -1):
        limit = len(array)

    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if(left < limit and array[left] > array[largest]):
        largest = left

    if(right < limit and array[right] > array[largest]):
        largest = right

    if(largest != root):
        swap(array, root, largest)
        heapify(array, largest, limit)


# Time complexity:  O(n*log(n))
# Space complexity: O(1)
def heap_sort(array):
    print("--- Heap Sort")

    # Transform the array into a max-heap
    for i in range(len(array) // 2 - 1, -1, -1):
        heapify(array, i)
    
    # Takes the largest item from the max-heap and inserts it in order at the end of the array
    for i in range(len(array) - 1, 0, -1):
        heapify(array, 0, i + 1)
        swap(array, 0, i)


if __name__ == "__main__":
    array = [3, 12, 5, 4, 11, -1, 144, -40, 21, 22]
    heap_sort(array)
    print(array)