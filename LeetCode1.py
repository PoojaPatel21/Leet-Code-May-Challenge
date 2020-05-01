class Solution:
    def firstBadVersion(self, n):
        # ls = i for i in range(1,n+1) if (isBadVersion(i))]
        # return ls[0]
        if(n==1):
            return 1
        else:
            end = n
            begin = 1 
           
            while(begin<end):
                mid = (begin+end)/2
                if(isBadVersion(mid)):
                    end = mid                 
                else:
                    begin = mid + 1
              
            return int(begin)
                
                
        