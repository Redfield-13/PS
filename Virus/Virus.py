#!/usr/bin/env python3
s = int(input())
v = []
for i in range(s):
    l = str(input())
    v.append(l)
for i in v:
    f = 0
    o=[]
    j=''
    for l in i:
        if l!= '#':
            o.append(l)
            j=j+str(l)
a = '' 
print(j)           
for i in range(len(j)-1):
  a = a  
  a = a+j[i]
print(a)      
         






#p = ['bvgvgg','786']
#print(p)
#print(str(p[0])+str(p[1]))
