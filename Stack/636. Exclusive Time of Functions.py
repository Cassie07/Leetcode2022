class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        res = [0 for i in range(n)]
        
        stack = []
        prev = 0
        for i in logs:
            fn_id, types, time = i.split(':')
            time = int(time)
            fn_id = int(fn_id)
            
            if types == 'start':
                
                if stack:
                    res[stack[-1]] += time - prev
                stack.append(fn_id)
                prev = time
            else:
                res[stack.pop()] += time - prev + 1
                prev = time + 1
                
        return res
