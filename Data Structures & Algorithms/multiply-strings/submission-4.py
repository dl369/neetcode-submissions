class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        if len(num1) < len(num2):
            temp = num1
            num1 = num2
            num2 = temp
        
        len1 = len(num1)
        len2 = len(num2)

        res = [0] * (len1 + len2)

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len2):
            for j in range(len1):
                total = int(num1[j]) * int(num2[i]) + res[i + j]

                res[i + j] = total % 10
                res[i + j + 1] += total // 10
        
        while len(res) > 1 and res[-1] == 0:
            res.pop()
            
        return "".join(map(str, reversed(res)))
