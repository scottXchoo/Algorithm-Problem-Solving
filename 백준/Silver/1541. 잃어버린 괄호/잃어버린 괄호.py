exps = input().split('-')
nums = []
for exp in exps:
    temp = exp.split('+')
    sums = 0
    for j in temp:
        sums += int(j)
    nums.append(sums)
    
n = nums[0]
for i in range(1, len(nums)):
    n -= nums[i]
    
print(n)