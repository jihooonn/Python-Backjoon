answer1 = input()
answer2 = input()
answer3 = input()

answer1_list = list(answer1)
answer2_list = list(answer2)
answer3_list = list(answer3)

if answer1_list[0] and answer2_list[0] and answer3_list[0] == ' ':
    return False
if answer1_list[-1] and answer2_list[-1] and answer3_list[-1] == ' ':
    return False 
print(answer1, answer2, answer3, sep = '\n')