N = int(input())
for i in range(N):
    S, R = input().split()
    for j in range(len(R)):
        New_str = R[j] * int(S)
        print(New_str, end = "")
    print('') 
    # AAABBBCCC와 /////HHHHHTTTTTPPPPP 간의 줄 간격이 생성되지 않는다.
