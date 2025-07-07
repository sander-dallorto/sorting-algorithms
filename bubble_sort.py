def bubble_sort(nums):
    swapping = True
    end = len(nums)

    while swapping == True:
        
        swapping = False

        for i in range(1, end):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True

        end -= 1

    return nums

def main():
    # Test case 1
    list1 = [5, 7, 3, 6, 8]
    print(f"Original list: {list1}")
    sorted_list1 = bubble_sort(list1)
    print(f"Sorted list: {sorted_list1}\n")

    # Test case 2
    list2 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    print(f"Original list: {list2}")
    sorted_list2 = bubble_sort(list2)
    print(f"Sorted list: {sorted_list2}\n")

    # Test case 3
    list3 = []
    print(f"Original list: {list3}")
    sorted_list3 = bubble_sort(list3)
    print(f"Sorted list: {sorted_list3}\n")

    # Test case 4
    list4 = [1]
    print(f"Original list: {list4}")
    sorted_list4 = bubble_sort(list4)
    print(f"Sorted list: {sorted_list4}\n")

if __name__ == "__main__":
    main()
