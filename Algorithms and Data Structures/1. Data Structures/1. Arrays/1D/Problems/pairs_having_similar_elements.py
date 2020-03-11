"""Given an array, A, having  integers A1 AX...An.Two elements of the array Ai and Aj are called similar iff Ai = Aj + 1 or Aj = Ai + 1 .
Also, the similarity follows transitivity. If Ai and Aj are similar and Aj and Ak are similar, then Ai and Ak are also similar. 
Note: i, j, and k are all distinct.

You need to find number of pairs of indices (i, j) such that i < j and Ai is similar to Aj.

Input

The first line contains a single integer N denoting number of elements in the array.
The second line contains N space separated integers where i-th elements indicate Ai.

Output

Output the number of pairs of indices (i, j) such that i < j and Ai is similar to Aj in a single line.
"""


def SimilarElementsPairs(A):
    sorted_list = sorted(A)
    similar = False
    ans = 0
    count = 0
    prev = sorted_list[0]
    for elem in sorted_list:
        if elem == prev:
            count += 1
        elif prev+1 == elem:
            count += 1
            similar = True
        else:
            if similar:
                ans += (count * (count-1)) // 2
                similar = False
            count = 1
        prev = elem
    if similar:
        ans += (count * (count-1)) // 2
    return ans


l = [x for x in range(100)]

out_ = SimilarElementsPairs(l)
print(out_)
