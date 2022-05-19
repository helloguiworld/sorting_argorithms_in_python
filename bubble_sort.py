# Time complexity:  O(n²)
# Space complexity: O(1)
def bubble_sort(sort_list):
    print("--- Bubble Sort")
    
    for i in range(len(sort_list) - 1):
        for j in range(len(sort_list) - i - 1):
            if(sort_list[j] > sort_list[j + 1]):
                swap(sort_list, j, j + 1)


def swap(array, a, b):
    (array[a], array[b]) = (array[b], array[a])


if __name__ == "__main__":
    sort_list = [3, 12, 5, 4, 11]
    bubble_sort(sort_list)
    print(sort_list)