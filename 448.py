# 448.找到数组中消失的数字
'''
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = list(range(1, len(nums)+1))
        return list(set(out)-set(nums))

if __name__ == '__main__':
    solution = Solution()
    x = [4,3,2,7,8,2,3,1]
    y = solution.findDisappearedNumbers(x)
    print(y)