def merge_cort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_cort(left)
        merge_cort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
               nums[k] = left[i]
               i += 1
            else:
               nums[k] = right[j]
               j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
             
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list_1 = [8, 75, 21, 45, 24, 56, 65, 54, 35, 7, 53, 4, 34, 2, 42, 17]
print(list_1)

merge_cort(list_1)
print(list_1)

