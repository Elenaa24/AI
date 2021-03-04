def test():
    assert gen_nr(4) == [[1], [1, 0], [1, 0, 0], [1, 1]]
    assert gen_nr(5) == [[1], [1, 0], [1, 0, 0], [1, 0, 1], [1, 1]]
    assert gen_nr(10) == [[1], [1, 0], [1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1], [1, 0, 1, 0], [1, 1], [1, 1, 0], [1, 1, 1]]

def get_nr(arr):

    ans = 0
    lg = len(arr)

    for i in range(lg):
        if arr[i] == 1:
            ans += (1 << (lg - i - 1))

    return ans

def gen_nr(n, crt = [1]):
    #input: crt - o lista ce contine 1, n - nr intreg
    #output: genereaza posibile solutii 
    sol = [crt]
    
    for i in range(2):
        nxt = crt + [i]
        if get_nr(nxt) <= n:    
            sol += gen_nr(n, nxt)
    return sol

#citesc n
test()
n = int(input())
print(gen_nr(n))