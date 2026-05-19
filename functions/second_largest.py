def second_largest(nums):
    largest = 0
    second_largest = 0
    for i in nums:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    return second_largest
nums = [3,1,4,1,5,9,2,6,5,3,5]
print(second_largest(nums))
