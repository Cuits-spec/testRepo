# 100以内斐波那契数列
# a = 0
# b = 1
# while a < 100:
#     print(a)
#     a,b = b,b+a

# 简单冒泡排序
nums = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(nums)-1):
    for j in range(len(nums)-1-i):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
print(nums)
