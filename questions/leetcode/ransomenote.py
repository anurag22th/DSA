'''
https://leetcode.com/problems/ransom-note/
'''

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''mag_count = Counter(magazine)
        for ch in ransomNote:
            if mag_count[ch] > 0:
                mag_count[ch] -= 1
            else:
                return False
        return True'''
        if len(set(ransomNote)) > len(set(magazine)):
            return False
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True