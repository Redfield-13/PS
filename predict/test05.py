dayz = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
half_cases = int(input())
cases = []
for i in range(half_cases*2):
    if i%2 ==0:
     one = input()
     cases.append(one)
    else:
        numList = list(int(num) for num in input().strip().split())[:7]
        #one = list(input())
        cases.append(numList)
#print(cases)
#print(len(cases[1]))
for i in range(0,len(cases),2):
    print("start")
    #print(i)
    if i == half_cases*2:
        break
    #print(i)
    #print(cases[i])
    #print(i)
    left = int(cases[i])
    sub = 0
    while sub < left:
     for l in range(0,7,1):
        sub = sub +int(cases[i][l])
        #minus = int(two)
        ##print(two)
        #print(minus)
        # if sub >= left :
        #     minus = left
        #     #print(left)
        # #print(minus)
        # left = left - minus
        #print(left)
        ##print(left)
        if sub >= left:
            print(dayz[l])
            break
