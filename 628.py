# 628.三个数的最大乘积
'''
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
'''
import heapq
class Solution(object):           
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        else:
            max_three = heapq.nlargest(3, nums)
            min_two = heapq.nsmallest(2, nums)
            return max(max_three[0]*max_three[1]*max_three[2], max_three[0]*min_two[0]*min_two[1])



    
                
