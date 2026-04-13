class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        mpp = defaultdict(list)
        n = len(ppid)
        for i in range(n):
            mpp[ppid[i]].append(pid[i])
        
        seen = set()
        seen.add(kill)
        def dfs(process_id):

            for child in mpp[process_id]:
                if child not in seen:
                    seen.add(child)
                    dfs(child)
        dfs(kill)

        return list(seen)
