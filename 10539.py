A_len = int(input())
B_Element = list(map(int, input().split()))
A_list = []
for i in range(A_len):
    
    if i == 0:
        A_list.append(B_Element[i] )
    else:    
        A_list.append(B_Element[i] * (i + 1) - B_Element[i-1] * i )
print(*A_list, sep = " ")