import time
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
dayz = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
# start_time = time.time()
for i in range(0,half_cases*2,2):
    tests_per_week = 0
    for l in range(7):
        tests_per_week = tests_per_week + int(cases[i+1][l])
    print(tests_per_week)
    multi = tests * ((int(cases[i])//tests)-1)
    print(multi)
    while multi > int(cases[i]):
        for v in range(0,7,1):
          minus = (7 - (v%7))-1
          multi = multi - cases[i+1][minus]
          if multi <= int(cases[i]):
              print(minus)
              break
    print(minus)
    print(dayz[minus])
# print('%s seconds'%(time.time()-start_time))
