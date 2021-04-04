tests = int(input())
viruses = []
for l in range(tests):
    one = input()
    viruses.append(one)
for virus in viruses:
    dayz = 0
    new_virus = ""
    for i in virus:
        if i != '#':
         new_virus = new_virus + i
    survived = True
    while len(new_virus) > 0:
           new_virus02 = new_virus.split('LR')
           dayz = dayz + 1
           if new_virus02[0] == new_virus and new_virus02[0] != '':
               survived = False
               break
           new_virus = ''
           for i in new_virus02:
                 if i != '':
                   new_virus = new_virus + i
    if survived :
        print(dayz)
    else:
        print('Unfortunately We are doomed!')
