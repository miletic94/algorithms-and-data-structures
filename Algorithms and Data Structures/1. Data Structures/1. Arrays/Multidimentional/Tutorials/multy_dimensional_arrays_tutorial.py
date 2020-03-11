import numpy as np
"""Transposing 2D list"""
"""Using Loop"""
l1 = [
    [13, 4, 8, 14, 1],
    [9, 6, 3, 7, 21],
    [5, 12, 17, 9, 3]
]
l2 = []
for i in range(len(l1[0])):
    row = []
    for j in l1:
        row.append(j[i])
    l2.append(row)
print(l2)

"""Using List Comprehention"""
l2 = [[row[i] for row in l1] for i in range(len(l1[0]))]
print(l2)

"""Using numpy"""
l2 = np.transpose(l1)
print(l2)
