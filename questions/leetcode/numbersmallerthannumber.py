'''
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
'''
def smallerNumbersThanCurrent(self, nums):
        """
        lst = []
        for i in range(len(nums)) :
            c = 0
            for j in range(len(nums)) :
                if(nums[i]>nums[j]) : c += 1
            lst.append(c)
        return lst
        """
        #sorted ka index mera count hai
        temp = sorted(nums)
        d = {}
        result = []
        for i,n in enumerate(temp):
            if n not in d:
                 d[n] = i
        for i in nums :
            result.append(d[i])
        return result
        