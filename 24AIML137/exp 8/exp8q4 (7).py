def list_sum(nums):
    sum=0
    for i in nums:
        sum+=i
    return sum

nums=[1,2,3,4,5,6,7,8,9,10]
print(list_sum(nums))