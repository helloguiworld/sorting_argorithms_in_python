from swap import swap

# Time complexity:  O(n²)
# Space complexity: O(1)
def bubble_sort(array):
    print("--- Bubble Sort")
    
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if(array[j] > array[j + 1]):
                swap(array, j, j + 1)


if __name__ == "__main__":
    array = [3, 12, 5, 4, 11, -1, 144, -40, 21, 22]
    bubble_sort(array)
    print(array)