vowel = ['A','E','I','O','U']
def check_tag(s):
    if s[2] in vowel:
        return 'invalid'
    num = s[0:2]+s[3:6]+s[7:]
    #print(num)
    for i in range(len(num)-1):
        if (int(num[i])+int(num[i+1]))%2 != 0:
            print(num[i],num[i+1])
            return 'invalid'
    return 'valid'

tag = input()
print(check_tag(tag))
