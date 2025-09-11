'''
https://leetcode.com/problems/fibonacci-number/
'''

def fib(self, n: int) -> int:
        '''if n <= 1:
            ans = n
        else:
            ans =  self.fib(n-1) + self.fib(n-2)
        return ans'''
        if n <= 1:
            return n
        f = [0] * (n + 1)

        # 0th and 1st numbers of the series are 1
        f[0] = 0
        f[1] = 1

        for i in range(2, n + 1):
            # Add the previous 2 numbers in the series and store it
            f[i] = f[i - 1] + f[i - 2]

        return f[n]