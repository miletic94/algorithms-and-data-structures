"""
Having a good previous year, Monk is back to teach algorithms and data structures.
This year he welcomes the learners with a problem which he calls "Welcome Problem".
The problem gives you two arrays A and B (each array of size N) and asks to print
new array C such that:
C[i] = A[i] + B[i]
"""

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 3, 2, 10]


def add_columns(l1, l2):
    s = []
    for i in range(len(l1)):
        s.append(l1[i] + l2[i])
    return s


print(add_columns(l1, l2))
