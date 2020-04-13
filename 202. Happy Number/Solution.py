class Solution:
    def nex(self, n: int) -> int:
        total = 0
        while n>0:
            total += (n%10)**2
            n//=10
        return total
    
    def isHappy(self, n: int) -> bool:
        s = set()
        while n > 1 and n not in s:
            s.add(n)
            n = self.nex(n)
        return n==1 
