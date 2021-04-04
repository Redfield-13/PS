import copy

inputs = list(int(num) for num in input().strip().split())[:4]

num_of_points = int(inputs[0])
desired_height = int(inputs[1])
pirall_cost = int(inputs[2])
arch_cost = int(inputs[3])
points = []
for i in range(num_of_points):
    numList = list(int(num) for num in input().strip().split())[:2]
    points.append(numList)

for i in range(num_of_points):
    pirall_height = desired_height - points[i][1]
    if not(i > num_of_points-2):
        distance = points[i+1][0]-points[i][0]
        arch_radius = distance/2
    if arch_radius > pirall_height:
        print('Impossible')
        exit()

overall_piralls_length = 0
overall_arch_length = 0
for i in range(num_of_points):
    pirall_height = desired_height - points[i][1]
    overall_piralls_length = overall_piralls_length + pirall_height
    if not(i > num_of_points-2):
        distance = points[i+1][0]-points[i][0]
        overall_arch_length = overall_arch_length + (distance*distance)

total_cost = (overall_arch_length*arch_cost)+(overall_piralls_length*pirall_cost)
print('')
print('')
print('')
print(total_cost)
