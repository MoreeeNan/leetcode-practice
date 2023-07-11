# 最大子序列交替和
from itertools import combinations

class Solution(object):
    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)

    @ staticmethod
    def AlternatingSum(x):
        sum = 0
        for i in range(len(x)):
            sum += x[i] if i % 2 == 0 else -x[i] 
        return sum
    
    def maxAlternatingSum(self):
        maxSum = self.AlternatingSum(self.nums)
        for i in range(1, self.len):
            for c in combinations(self.nums, i):
                temp_sum = self.AlternatingSum(c)
                maxSum = temp_sum if maxSum <= temp_sum else maxSum
        return maxSum

if __name__ == '__main__':
    x = [4,2,5,3]
    solution = Solution(x)
    y = solution.maxAlternatingSum()
    print(y)