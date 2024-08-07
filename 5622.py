"""
s = list(input())
s_alpha = { 2 : 'ABC', 3 : 'DEF', 4 : 'GHI', 5 : 'JKL',
           6 : 'MNO', 7 : 'PQRS', 8 : 'TUV', 9 : 'WXYZ'}
for value in s_alpha.values():
    s_alpha_value = list(value)
    if len(s_alpha_value) == 3:
        for i in s:
            if i == s_alpha_value[0] or i == s_alpha_value[1] or i == s_alpha_value[2]:
                print()
"""          
        
    
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)
       