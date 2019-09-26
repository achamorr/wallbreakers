class Solution:
    def isSelfDividing(self, n):
        if "0" in str(n): return False
        li = [int(j) for j in str(n)]
        for i in li:
            if n%i != 0:
                return False
        return True
            
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        li = []
        for i in range(left, right+1):
            if (self.isSelfDividing(i)):
                li.append(i)
        return li