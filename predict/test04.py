#operations = 0
dayz = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
half_cases = int(input())
#operations = operations + 2
cases = []
#operations = operations + 2
for i in range(half_cases*2):
    #operations = operations + 2
    if i%2 ==0:
     #operations = operations + 2
     one = input()
     #operations = operations + 2
     cases.append(one)
    # operations = operations + 2
    else:
        #operations = operations + 2
        numList = list(int(num) for num in input().strip().split())[:7]
        #operations = operations + 2
        #one = list(input())
        cases.append(numList)
        #operations = operations + 2
#print(cases)
#print(len(cases[1]))
#operations = operations + 2
for i in range(0,len(cases),2):
    print("start")
    #operations = operations + 2
    #print(i)
    if i == half_cases*2:
        #operations = operations + 2
        break
        #operations = operations + 2
    #print(i)
    #print(cases[i])
    #print(i)
    left = int(cases[i])
    sub = 0
    #operations = operations + 2
    while sub < left:
     #operations = operations + 2
     for l in range(0,7,1):
        #operations = operations + 2
        sub = sub +int(cases[i][l])
        #operations = operations + 2
        #minus = int(two)
        #operations = operations + 2
        ##print(two)
        #print(minus)
        # if sub >= left :
        #     #operations = operations + 2
        #     minus = left
        #     #operations = operations + 2
        #     #print(left)
        # #print(minus)
        # left = left - minus
        #operations = operations + 2
        #print(left)
        ##print(left)
        if sub >= left:
            #operations = operations + 2
            print(dayz[l])
            #operations = operations + 3
            #print(operations)
            #operations = operations + 3
            break
    #break144963050  30 15 25 4 10 25 30
#print(operations)
