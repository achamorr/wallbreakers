class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        #print (num)
        complement = ""
        for i in num:
            if i == '0':
                complement += '1'
            else:
                complement += '0'
        return int(complement,2)