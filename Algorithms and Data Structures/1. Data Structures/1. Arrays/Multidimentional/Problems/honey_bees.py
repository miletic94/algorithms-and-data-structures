"""
The Queen Bee has asked the Worker Bees to write a program to answer queries 
regarding her T hives. A hive can be visualized using a rectangular matrix of 
size N X M . Figure below shows the coordinates of each cell. Each cell contains 
honey which is depicted by a number in the corresponding 2D array ( <= 100).

https://he-s3.s3.amazonaws.com/media/uploads/7546f25.jpg

The Queen Bee asks Q queries which need to be answered, they are of the following 
types :

1 X Y -- To sum the honey over all cells which are at a 1-hop distance from 
cell (X, Y) i.e. it takes only 1 hop in any direction from cell (X, Y) to reach 
these

2 X Y -- To sum the honey over all cells which are at a 2-hop distance from 
cell (X, Y) i.e. it takes only 2 hops in any direction from cell (X, Y) to reach 
these

A hop is defined as moving from a cell (X, Y) to a cell it shares a common edge with
i.e. its immediate neighbor.

You'll be given T, the number of testcases, followed by N, M, the size of the 
matrix/hive. The next N lines contain M integers each consisting the honey amount 
in each cell. This is followed by Q, the number of queries. The next Q lines are of 
the type 1 X Y and 2 X Y where (X, Y) is the cell location.

Output every query in a new line.

1 <= T <= 10

1 <= N, M, Q <= 200

0 <= X < N and 0 <= Y < M
"""

hive = [
    [0.0, 0.1, 0.2, 0.3, 0.4],
    [1.0, 1.1, 1.2, 1.3, 1.4],
    [2.0, 2.1, 2.2, 2.3, 2.4],
    [3.0, 3.1, 3.2, 3.3, 3.4],
    [4.0, 4.1, 4.2, 4.3, 4.4]
]

"""
The Queen Bee has asked the Worker Bees to write a program to answer queries 
regarding her T hives. A hive can be visualized using a rectangular matrix of 
size N X M . Figure below shows the coordinates of each cell. Each cell contains 
honey which is depicted by a number in the corresponding 2D array ( <= 100).

https://he-s3.s3.amazonaws.com/media/uploads/7546f25.jpg

The Queen Bee asks Q queries which need to be answered, they are of the following 
types :

1 X Y -- To sum the honey over all cells which are at a 1-hop distance from 
cell (X, Y) i.e. it takes only 1 hop in any direction from cell (X, Y) to reach 
these

2 X Y -- To sum the honey over all cells which are at a 2-hop distance from 
cell (X, Y) i.e. it takes only 2 hops in any direction from cell (X, Y) to reach 
these

A hop is defined as moving from a cell (X, Y) to a cell it shares a common edge with
i.e. its immediate neighbor.

You'll be given T, the number of testcases, followed by N, M, the size of the 
matrix/hive. The next N lines contain M integers each consisting the honey amount 
in each cell. This is followed by Q, the number of queries. The next Q lines are of 
the type 1 X Y and 2 X Y where (X, Y) is the cell location.

Output every query in a new line.

1 <= T <= 10

1 <= N, M, Q <= 200

0 <= X < N and 0 <= Y < M
"""

hive = [
    [0.0, 0.1, 0.2, 0.3, 0.4],
    [1.0, 1.1, 1.2, 1.3, 1.4],
    [2.0, 2.1, 2.2, 2.3, 2.4],
    [3.0, 3.1, 3.2, 3.3, 3.4],
    [4.0, 4.1, 4.2, 4.3, 4.4]
]

cell = (0, 1)


def cell1(x):
    if x[1] % 2 == 0:
        a = []
        for i in range(x[0]-1, x[0]+2):
            for j in range(x[1]-1, x[1]+2):
                if i == x[0] and j == x[1] or (i == x[0] + 1 and (j == x[1] - 1 or j == x[1] + 1)) or i == -1 or j == -1:
                    pass
                else:

                    a.append((i, j))
        return a

    if x[1] % 2 != 0:
        b = []
        for i in range(x[0]-1, x[0]+2):
            for j in range(x[1]-1, x[1]+2):
                if i == x[0] and j == x[1] or (i == x[0] - 1 and (j == x[1] - 1 or j == x[1] + 1)) or i == -1 or j == -1:
                    pass
                else:

                    b.append((i, j))
        return b


x = cell1(cell)


def cell2(x):
    ll = []
    l = []
    for i in x:
        ll.append(cell1(i))
    print(sorted(x))
    for i in ll:
        for j in i:
            l.append(j)
    l = list(set(l))
    print(sorted(l))
    for i in l:
        if i in x:
            l.remove(i)
    l.remove(cell)
    print(sorted(l))


cell2(x)
