class Solution:
    def alphanumeric(self, s):
        return ( "".join(i for i in s if i.isalnum()) )
        
    
    def isPalindrome(self, s: str) -> bool:
        s = self.alphanumeric(s.lower())
        l_index = len(s)-1
        for i in range(int(len(s)/2)):
            if s[i] != s[l_index -i]:
                return False
        return True