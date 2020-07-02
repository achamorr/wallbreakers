class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse = False)
        g.sort(reverse = False)
        happyKids = 0
        
        
        for kidgreed in g:
            for i,cookie in enumerate(s):
                if kidgreed <= cookie:
                    happyKids +=1
                    del s[i]
                    break
        return happyKids