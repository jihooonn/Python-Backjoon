str = list(input())
eng = 'abcdefghijklmnopqrstuvwxyz'

for i in eng:
    if i in str:
        print(str.index(i), end = ' ')
    else:
        print(-1, end = ' ')