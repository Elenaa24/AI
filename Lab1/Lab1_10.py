def test():
    assert index_mat([[0, 0, 0, 1], [0, 0, 1, 1]]) == 2
    assert index_mat([[0, 0, 0, 1], [0, 0, 0, 0]]) == 1

def index_mat(mat):
    #input: mat-matrice
    #output: nr intreg
    #functia cauta linia cu cei mai multi 1, afla nr lor print gasirea (cautare binara) primei pozitii pe care se afla 1
    n = len(mat)

    best = len(mat[0]) + 1
    pos_best = -1

    for i in range(n):
        lo = 0
        hi = len(mat[i]) - 1

        ans = hi + 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if mat[i][mid] == 1:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        if ans < best:
            best = ans
            pos_best = i

    #returnez +1 pt ca am indentarea e de la 0
    return pos_best+1

test()
#citesc dimensiunile matricii
n = int(input())
m = int(input())

mat = []
#citesc matricea
for i in range(n):
    line = [int(x) for x in input().strip().split()]
    mat.append(line)
#afisez solutia
print(index_mat(mat))