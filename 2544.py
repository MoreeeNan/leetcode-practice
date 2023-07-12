# 交替数字和

class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = len(str(n))
        sign = 1
        result = 0
        while i>=1:
            temp = 10 ** (i-1)
            result += sign * (n//temp)
            n %= temp
            i -= 1
            sign *= -1
        return result
        
        
if __name__ == '__main__':
    solution = Solution()
    n = 521
    y = solution.alternateDigitSum(n)
    print(y)