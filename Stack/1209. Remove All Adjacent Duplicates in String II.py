class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        res = []
        
        for i in s:
            if res:
                if i == res[-1][0]:
                    res[-1][1] += 1
                    if res[-1][1] == k:
                        res.pop()
                else:
                    res.append([i,1])
            else:
                res.append([i,1])
                
        return ''.join(i*n for i,n in res)
