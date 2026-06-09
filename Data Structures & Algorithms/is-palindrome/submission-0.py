class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        res = []

        for e in s:
            if e.isalnum():
                lst.append(e.lower())
        print(lst)

        for i in range( len(lst) - 1, -1, -1):
                res.append(lst[i])
        print(res)

        if res == lst:
            return True
        else:
            return False