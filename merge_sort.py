def merge(array, left_start, left_end, right_start, right_end):
    merge_start = left_start
    # merge_end = right_end

    left_array = array[left_start:left_end + 1]
    right_array = array[right_start:right_end + 1]
    left_start = right_start = 0
    left_end = len(left_array)
    right_end = len(right_array)
    # print(left_array, left_start, left_end)
    # print(right_array, right_start, right_end)
    
    # Merge left and right arrays comparing their smallest elements
    while(left_start < left_end and right_start < right_end):
        if(left_array[left_start] <= right_array[right_start]):
            array[merge_start] = left_array[left_start]
            left_start += 1
        else:
            array[merge_start] = right_array[right_start]
            right_start += 1
        
        merge_start += 1

    # Check if any element of the left array was left
    while(left_start < left_end):
        array[merge_start] = left_array[left_start]
        left_start += 1
        merge_start += 1

    # Check if any element of the right array was left
    while(right_start < right_end):
        array[merge_start] = right_array[right_start]
        right_start += 1
        merge_start += 1

    # An alternative way of merge the left and right arrays,
    #   without need to check if any item of them was left
    # while(merge_start <= merge_end):
    #     if(right_start >= right_end or 
    #         (left_start < left_end and left_array[left_start] <= right_array[right_start])):
    #         array[merge_start] = left_array[left_start]
    #         left_start += 1
    #     else:
    #         array[merge_start] = right_array[right_start]
    #         right_start += 1
    #     merge_start += 1


# Time complexity:  O(n*log(n))
# Space complexity: O(n)
def merge_sort(array, start = 0, end = -1):
    if(end == -1):
        print("--- Merge Sort")
        end = len(array) - 1

    # print(start, end)
    # print(array[start:end + 1])
    
    if(start < end):
        middle = start + (end - start) // 2

        merge_sort(array, start, middle)
        merge_sort(array, middle + 1, end)

        merge(array, start, middle, middle + 1, end)
        # print(array[start:end + 1])


if __name__ == "__main__":
    array = [3, 12, 5, 4, 11, -1, 144, -40, 21, 22]
    merge_sort(array)
    print(array)