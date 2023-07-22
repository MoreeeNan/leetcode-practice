# 860.柠檬水找零
'''
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 第一个不是5美元，无法找零
        if bills[0] != 5:
            return False
        else:
            # 初始化
            cash10 = 0
            cash5 = 1
            for i in range(1, len(bills)):
                # 付5美元，没任何问题
                if bills[i] == 5:
                    cash5 += 1
                # 付10美元，需要有一张5美元，否则无法找零
                elif bills[i] == 10:
                    if cash5 < 1:
                        return False
                    else:
                        cash5 -= 1
                        cash10 += 1
                else:
                    # 付20美元，要么有1张5和一张10，要么有3张5，否则无法找零
                    if cash5 >= 1 and cash10 >=1:
                        cash5 -= 1
                        cash10 -= 1
                    elif cash5 >= 3:
                        cash5 -= 3
                    else:
                        return False
            return True


                    

