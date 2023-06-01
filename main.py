num_1=int(input())
num_2=int(input())
if num_1 > num_2:
    s=0
    for i in range(num_2, num_1+1):
        s += i
    print(s)
elif num_2 > num_1:
    s1 = 0
    for i1 in range(num_1, num_2+1):
        s1 += i1
    print(s1)




