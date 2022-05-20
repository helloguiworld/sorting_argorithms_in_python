from swap import swap

# Time complexity:  O(n²)
# Space complexity: O(1)
def selection_sort(array):
    print("--- Selection Sort")

    for i in range(len(array) - 1):
        maior = 0
        for j in range(1, len(array) - i):
            if(array[maior] < array[j]):
                maior = j
        
        swap(array, maior, len(array) - i - 1)


if __name__ == "__main__":
    array = [3, 12, 5, 4, 11, -1, 144, -40, 21, 22]
    selection_sort(array)
    print(array)