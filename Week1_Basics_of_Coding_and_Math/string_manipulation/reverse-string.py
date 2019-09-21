class Solution:
    def reverseString(self, word: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(int((len(word)/2))):
            #need to swap
            tempChar = word[i]
            word[i] = word[len(word)-1-i]
            word[len(word)-1-i] = tempChar
        return word
            
        