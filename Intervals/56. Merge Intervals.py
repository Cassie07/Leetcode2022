class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        prev = 0
        for interval in sorted(intervals):        
            if not res:
                res.append(interval)
            else:
                start, end = interval[0], interval[1]
                prev_start, prev_end = res[prev][0],res[prev][1]
                
                if start > prev_end:
                    res.append(interval)
                    prev += 1
                elif end > prev_end:
                    res[prev][1] = end
                elif end<= prev_end:
                    continue             
        return res
                
