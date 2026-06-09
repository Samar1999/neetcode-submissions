class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for e in s:
            if e == '(':
                res.append(')')
            elif e == '{':
                res.append('}')
            elif e == '[':
                res.append(']')
            else:
                if not res or e != res.pop():
                    return False

        return not res
                 
                
        