import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        flag = False
        limit = int(math.sqrt(c)) + 1
        i = 0
        j = int(math.sqrt(c))
        while i <= j:
            if i * i + j * j == c:
                return True
                flag = True
                break
            elif i * i + j * j < c:
                i += 1
            else:
                j -= 1

        if not flag:
            return False
