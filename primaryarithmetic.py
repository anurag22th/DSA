def carry_count(x,y):
    count = 0
    carry = 0#count > 10 ke liye but jo 10 ho gaya usko kaun uthayega? 
    #isliye carry liya
    while x or y:
        if (x%10) + (y%10)+carry > 9:
            count += 1
            carry = 1
        else:
            carry = 0
        x //= 10
        
        y //= 10
    if count == 0:
        print('No carry operation.')
    elif count == 1:
        print(f'{count} carry operation.')
    else:
        print(f'{count} carry operations.')
        

while True:
    num1, num2 = map(int, input().split())
    if num1 == num2 == 0:
        break
    carry_count(num1, num2)