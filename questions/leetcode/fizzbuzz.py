'''
https://leetcode.com/problems/fizz-buzz/
'''
def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            retStr = ""
            divis = False
            if i % 3 == 0:
                retStr += "Fizz"
                divis = True
            if i % 5 == 0:
                retStr += "Buzz"
                divis = True
            if not divis:
                retStr += str(i)
            result.append(retStr)
        return result
        '''
        st = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                st.append("FizzBuzz")
            elif i%3 == 0:
                st.append("Fizz")
            elif i%5 == 0:
                st.append("Buzz")
            else:
                st.append(f"{i}")
        return st'''