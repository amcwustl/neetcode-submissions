class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {} 
        for i in s:
            s_map[i] = s_map.get(i, 0) + 1
        for i in t:
            t_map[i] = t_map.get(i, 0) + 1

        for key in s_map.keys():
            if s_map.get(key) != t_map.get(key):
                return False
            
        return True
        