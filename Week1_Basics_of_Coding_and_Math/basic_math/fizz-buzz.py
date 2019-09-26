class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        li = []
        for i in range(1,n+1):
            string = ""
            if i%3 == 0:
                string += "Fizz"
            if i%5 == 0:
                string += "Buzz"
            if len(string) > 0:
                li.append(string)
            else: 
                li.append(str(i))
        return li