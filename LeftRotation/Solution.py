#!/bin/python3



#fix the input parsing
nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))

front = a[d:]
back = a[:d]


new_array = front + back

final_array = [str(x) for x in new_array]
output = ' '.join(final_array)

print(output)