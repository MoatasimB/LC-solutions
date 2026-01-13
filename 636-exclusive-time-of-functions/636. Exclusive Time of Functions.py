class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        ans = [0] * n
        stack = [] #id, lastTime
        for i in range(len(logs)):
            log = logs[i].split(":")
            id = int(log[0])
            type_ = log[1]
            timeStamp = int(log[2])


            if type_ == "start":
                if stack:
                    prev_id, prev_time = stack[-1]

                    ans[prev_id] += timeStamp - prev_time
                stack.append([id, timeStamp])
            else:

                prev_id, prev_time = stack.pop()
                ans[prev_id] += timeStamp - prev_time + 1

                if stack:
                    stack[-1][1] = timeStamp + 1
        
        return ans
