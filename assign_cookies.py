class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookie_id = 0
        child_id = 0
        
        s.sort()
        g.sort()
        while child_id < len(g) and cookie_id < len(s):
            if s[cookie_id] >= g[child_id]:
                child_id += 1
            cookie_id += 1
        
        return child_id
