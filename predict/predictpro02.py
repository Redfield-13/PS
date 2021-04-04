
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
    left = int(mount)
    while left > 0:
        # for l in range(0,7,1):
        #    two = cases[cases.index(i)+1][l]
        #    minus = int(two)
        #    if minus > left :
        #        minus = left
        #    left = left - minus
        #    if left == 0:
        #        return dayz[l]
        #        break


for i in cases:
     if cases.index(i)%2 != 0:
        continue
     print(predict(cases[cases.index(i)],cases[cases.index(i)+1]))
        #if cases.index(i) == half_cases :
            #break
    #print(cases.index(i))
