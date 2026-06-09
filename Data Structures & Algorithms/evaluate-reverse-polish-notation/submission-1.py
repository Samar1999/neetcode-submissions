class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        val = 0
        for e in tokens:
            if e == '+':
                val = int(res[-2]) + int(res[-1])
                res.pop()
                res.pop()
                res.append(val) 
            elif e == '-':
                val = int(res[-2]) - int(res[-1])
                res.pop()
                res.pop()
                res.append(val)
            elif e == '*':
                val = int(res[-2]) * int(res[-1])
                res.pop()
                res.pop()
                res.append(val) 
            elif e == '/':
                val = int(res[-2]) / int(res[-1])
                res.pop()
                res.pop()
                res.append(val) 
            else:
                res.append(e)
        
        return int(res[-1])