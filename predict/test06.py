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
def predict(mount,days):
    '''
    e.g = [5,[1,8,19,30,23,0]]
    '''
    dayz = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
    tests = 0
    for i in range(7):
        tests = tests+cases[i][1][i]
    multi = tests * ((cases[i][0]//tests)+1)
    print(multi)
