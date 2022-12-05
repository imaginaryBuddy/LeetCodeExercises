class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1 : "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40:"XL", 50: "L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        res = ""
        numOfDig = len(str(num))
        d = 1
        for i in range(numOfDig): 
            digit = num % 10
            num = num // 10
            temp = "" 
            if digit != 9 and digit != 4:
                if digit >= 5 : 
                    temp = dict[5 * d] + temp
                    digit = digit - 5
                for i in range(digit):
                    temp = temp + dict[d]
                res = temp + res
            else :
                res = dict[digit*d] + res
            d = d*10 

        return res
