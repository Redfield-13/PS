nums  = [0,1]
n = int(input())
for i in range(2,n+1):
    nums.append(nums[i-1]+nums[i-2])

# print(nums)
print(nums[n])
