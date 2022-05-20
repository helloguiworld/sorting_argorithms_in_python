# Time complexity:  O(n²)
# Space complexity: O(1)
def insertion_sort(array):
    print("--- Insertion Sort")

    for i in range(1, len(array)):
        item = array[i]
        pos = i - 1
        while(pos >= 0 and item < array[pos]):
            array[pos + 1] = array[pos]
            pos -= 1
        
        array[pos + 1] = item


if __name__ == "__main__":
    array = [3, 12, 5, 4, 11, -1, 144, -40, 21, 22]
    insertion_sort(array)
    print(array)