import copy
tiles_num = int(input())
cases = []
for i in range(4):
    numList = list(int(num) for num in input().strip().split())[:tiles_num]
    cases.append(numList)
cases02 = copy.deepcopy(cases)
cases03 = []
for i in range(0,4,2):
    mins =  []
    pos  = []
    for l in range(tiles_num):
        mins.append(min(cases02[i]))
        gg = cases02[i].index(min(cases02[i]))
        pos.append(cases02[i+1][gg])
        cases02[i].remove(min(cases02[i]))
        del cases02[i+1][gg]
    cases03.append(mins)
    cases03.append(pos)

for i in range(tiles_num):
    if cases03[1][i] == cases03[3][i]:
        for l in range(tiles_num):
            if l == tiles_num-1:
                break
            if (cases03[1][l]-cases03[3][l] >= 2) and (cases03[2][l] == cases03[2][l+1]) :
                wp = cases03[3][i]
                cases03[3][i] = cases03[3][l]
                cases03[3][l] = wp
wpp = 0
wpp02 = 0
for i in range(tiles_num):
    if cases03[1][i] <= cases03[3][i]:
        print('impo')
        exit()
        break
    else:
        pos02 = []
        pos03 = []
        mm = []
        for o in  range(tiles_num):
            for l in range(tiles_num):
                if (cases03[1][o] == cases[1][l]) and (cases03[0][o] == cases[0][l]) and (wpp != l) :
                    # print(i,wpp,l)
                    pos02.append(l+1)
                    wpp = l
                    break
        print("")
        print("")
        print("")
        print("")
        print(*pos02)
        break
for i in range(tiles_num):
    if cases03[1][i] <= cases03[3][i]:
        print('impo')
        exit()
        break
    else:
        pos02 = []
        pos03 = []
        mm = []
        for o in  range(tiles_num):
            for l in range(tiles_num):
                if (cases03[3][o] == cases[3][l]) and (cases03[2][o] == cases[2][l]) and (wpp != l) :
                    # print(i,wpp,l)
                    pos03.append(l+1)
                    wpp = l
                    break
        print("")
        print(*pos03)
        break
