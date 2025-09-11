'''
https://leetcode.com/problems/valid-word/
'''
vowels  = set('aeiou')
cons = set('sdzxcvbnmlkjhgfdsqwrtyp')

def isValid(word: str) -> bool:
    if (len(word)>2 
    and word.isalnum() 
    and len(set(word.lower()).intersection(vowels))>0 
    and len(set(word.lower()).intersection(cons)))>0:
        return True
    return False