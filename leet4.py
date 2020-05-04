class Solution:
    def findComplement(self, num: int) -> int:
        num1 = bin(num)
        ls=[]
        k = str(num1)
        for i in range(len(k)-2):
            ls.append(k[i+2])
      
        for i in range(len(ls)):
            if(ls[i]=='0'):
                ls[i]=1
            else:
                ls[i]=0
        s = [str(i) for i in ls] 
      
    # Join list items using join() 
        res = "".join(s)
        sol = int(res,2)
        return sol
        