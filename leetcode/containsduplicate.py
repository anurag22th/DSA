'''
https://leetcode.com/problems/contains-duplicate/
'''
def containsDuplicate(self, nums: List[int]) -> bool:
        
        s = Counter(nums)
        for i in s.values():
            if i >= 2:
                return True
        return False

        return (len(set(nums)) != len(nums))