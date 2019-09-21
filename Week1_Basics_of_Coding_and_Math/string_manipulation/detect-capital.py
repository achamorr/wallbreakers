class Solution:
    def isCapitalLetter(self, char):
        if ord(char) >= 65 and ord(char) <= 90:
            return True
        else:
            return False
        
    def detectCapitalUse(self, word: str) -> bool:
        capitalCount = 0
        for char in word:
            if self.isCapitalLetter(char):
                capitalCount += 1
        if capitalCount == len(word) or capitalCount == 0 or (self.isCapitalLetter(word[0]) and capitalCount == 1):
            return True
        else:
            return False