"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8 3^2  10
21  22  23  24 5^2
..  ..  ..  ..  .. 7^2
"""

import numpy as np

input = 368078

def side_length(number):
    side = int(np.sqrt(number))+1
    if side %2 == 0:
        side = side + 1
    return side

side = side_length(input)

steps_to_reach_center_from_axis = (side-1)/2

axes = []
for i in range(4):
    axes.append(side**2 - ((side-1) * i)  - int(side/2)


steps_to_reach_axe_from_input = min([abs(axis - input) for axis in axes])

print(steps_to_reach_axe_from_input + steps_to_reach_center_from_axis)