class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for e in s:
            
            if e == '(':
                stack.append(')')
            elif e == '{':
                stack.append('}')
            elif e == '[':
                stack.append(']')
            else:
                if not stack or e != stack.pop():
                    return False

        return not stack