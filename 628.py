# 628.三个数的最大乘积
'''
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
'''
class Solution(object):
    @ staticmethod
    def find1stPositive(nums):
        # nums已经按照绝对值从大到小排列好
        for num in nums:
            if num > 0:
                return num
            
    @ staticmethod
    def find1stNegative(nums):
        # nums已经按照绝对值从大到小排列好
        for num in nums:
            if num < 0:
                return num
            
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums, key=abs, reverse=True)

        a,b,c = nums[0:3]
        if len(nums) == 3:
            return a*b*c
        else:
            # 正正负，找到下一个绝对值最大的正数令为c
            if a>0 and b>0 and c<0:
                c = self.find1stPositive(nums[3:])
            # 正负正，找到下一个绝对值最大的负数令为c
            elif a>0 and b<0 and c>0:
                c = self.find1stNegative(nums[3:])
            # 负正正，找到下一个绝对值最大的负数令为c
            elif a<0 and b>0 and c>0:
                c = self.find1stNegative(nums[3:])
            # 负负负，找到下一个绝对值最大的正数令为c
            elif a<0 and b<0 and c<0:
                c = self.find1stPositive(nums[3:])
            return a*b*c


    
                
