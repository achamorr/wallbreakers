class Solution:

    def lemonadeChange(self, bills):
        change = [0]
        for j,bill in enumerate(bills):
            able = False
            if bill > 5:
                remainder = bill - 5
                ogRemainder= bill
                #for i,ch in enumerate(change):
                i = 0
                while i < len(change):
                    ch = change[i]
                    print (remainder,change,i)
                    if remainder - ch == 0:
                        #print ("del %i",change[i])
                        del change[i]
                        able = True
                        change.insert(0,bill)
                        break
                    elif remainder - ch > 0: #still change to give
                        remainder -= ch
                        del change[i]
                        i = 0
                    else: #change too big
                        i+=1

                if not able:
                    return False
            elif bill == 5:
                change.append(bill)
            else:
                print ("Not enough for lemonade!")
            #print (able, change)
            
        return True
                    
                    

if __name__ == "__main__":
    print ("hi")
    s= Solution()
    t1 = s.lemonadeChange([10,10])
    t2 = s.lemonadeChange([5,5,10])
    t3 = s.lemonadeChange([5,5,10,10,20])
    t4 = s.lemonadeChange([5,5,5,10,20])
    t5 = s.lemonadeChange([5,5,5,5,10,5,10,10,10,20])
    print (t1,t2,t3,t4,t5)
    