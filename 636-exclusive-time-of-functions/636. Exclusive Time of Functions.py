class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        last_time = -1
        for i in range(len(logs)):
            log = logs[i].split(":")
            fid = int(log[0])
            ex = log[1]
            timestamp = int(log[2])

            if ex == "start":
                if stack:
                    prev_fid, prev_timestamp = stack[-1]
                    print(prev_fid, prev_timestamp)
                    ans[prev_fid] += timestamp - prev_timestamp
                stack.append([fid, timestamp])
            else:
                prev_fid, prev_timestamp = stack.pop()
                ans[prev_fid] += timestamp - prev_timestamp + 1
                if stack:
                    stack[-1][1] = timestamp + 1
        
        return ans
            
            


