import time
dayz = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATERDAY','SUNDAY']
case = [205109557,[947, 387, 984, 295, 53, 619, 964]]
left = case[0]
sub = 0
# while sub<left:
#  for i in range(len(case[1])):
#     sub = sub + case[1][i]
#     if sub >= left:
#         print(dayz[i])
#         break
tests = 0
start = time.time()
for i in range(len(case[1])):
    tests = tests + case[1][i]
# print(tests)
# print(case[0]//tests)
# print(tests*48273)
multi = tests * ((case[0]//tests)+1)
while multi > case[0]:
    for i in range(7):
      minus = (7 - (i%7))-1
      multi = multi - case[1][minus]
      if multi <= case[0]:
          break
print(dayz[minus])
end = time.time()
print('%s seconds'%(end-start))
# print(tests)
# 947 387 984 295 53 619 964
#day = case[1].find(i)
#[357226337,[10, 69, 255, 79, 121, 990, 576]]
