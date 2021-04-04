dayz = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATERDAY','SUNDAY']
case = [638415151,[979, 306, 923, 959, 745, 606, 778]]
left = case[0]
while  left > 0:
    for i in range(len(case[1])):
        two = case[1][i]
        if two >left:
            two =left
        left = left - two
        if left == 0:
            print(dayz[i])
            break

#day = case[1].find(i)
