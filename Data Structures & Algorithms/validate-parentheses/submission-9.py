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
                if stack and e == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack