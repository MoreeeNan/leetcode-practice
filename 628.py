# 628.三个数的最大乘积
'''
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
'''
class Solution(object):           
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        else:
            nums.sort(reverse=True)
            if nums[-1] > 0:
                # 全为正数
                return nums[0]*nums[1]*nums[2]
            elif nums[0] < 0:
                # 全为负数
                return nums[0]*nums[1]*nums[2]
            else:
                # 有正有负
                # 要么是三个最大正数相乘，要么是最大正数和两个最小负数的乘积
                a,b,c = nums[0:3]
                e,f = nums[-2:]
                return max(a*b*c,a*e*f)



    
                
