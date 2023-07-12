# 有效的括号

class Solution(object):       
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        else:           
            encode_dict = {'(':1, ')':-1, '{':2, '}':-2, '[':3, ']':-3}
            encode_list = []
            for i in range(len(s)):
                encode_list.append(encode_dict[s[i]])
                if i % 2 != 0 and encode_list[i]+encode_list[i-1] != 0:
                    return False
            return True
                    
        
    
if __name__ == '__main__':
    s = "{[]}"
    solution = Solution()
    out = solution.isValid(s)
    print(out)