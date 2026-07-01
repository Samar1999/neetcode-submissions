class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        res = []
        val = 0
        for e in tokens:
            if e == '+':
                a = res.pop()
                b = res.pop()
                res.append(b + a)
            elif e == '-':
                a = res.pop()
                b = res.pop()
                res.append(b - a)
            elif e == '*':
                a = res.pop()
                b = res.pop()
                res.append(b * a)
            elif e == '/':
                a = res.pop()
                b = res.pop()
                res.append(int(b / a))
            else:
                res.append(int(e))
        
        return res[-1]