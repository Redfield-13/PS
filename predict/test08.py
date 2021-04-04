half_cases = int(input())
cases = []
for i in range(half_cases*2):
    if i%2 ==0:
     one = input()
     cases.append(one)
    else:
        numList = list(int(num) for num in input().strip().split())[:7]
        cases.append(numList)
dayz = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
for i in range(0,half_cases*2,2):
    tests_per_week = 0
    over_all_tests = int(cases[i])
    for l in range(7):
        tests_per_week = tests_per_week + int(cases[i+1][l])
    o = 0
    ans = (tests_per_week * (over_all_tests//tests_per_week))-tests_per_week
    while ans < over_all_tests:
        for v in range(7):
            o = v
            ans = ans + cases[i+1][v]
            if ans >= over_all_tests:
                # print(o)
                break
    print(dayz[o])
