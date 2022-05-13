# Merge interval
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
                
        i, j = 0,0
        
        res = []
        
        while i<len(firstList) and j<len(secondList):
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
            
            if low <= high:
                res.append([low, high])
                
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
                
        return res  
            
            
# Two pointers
# class Solution:
#     def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
#             interval1 = firstList[i]
#             interval2 = secondList[j]
            
#             s1,e1 = interval1
#             s2,e2 = interval2

#             if e1 < s2:
#                 i += 1
#             elif e2 < s1:
#                 j += 1
#             else:   
#                 if s1 < s2:
#                     res.append([s2,min(e2,e1)])
#                     if e2 < e1:
#                         j += 1
#                     else:
#                         i += 1
#                 elif s2 < s1:
#                     res.append([s1,min(e2,e1)])
#                     if e1 < e2:
#                         i += 1
#                     else:
#                         j += 1
#                 else:
#                     res.append([s1, min(e2,e1)])
#                     if e1 > e2:
#                         j += 1
#                     elif e1 < e2:
#                         i += 1
#                     else:
#                         i += 1
#                         j += 1          
#         return res
