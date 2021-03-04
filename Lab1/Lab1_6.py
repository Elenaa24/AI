def test():
    assert max([1,2,3,4,5],5,3) == 3
    assert max([1,2,3,4,5],5,4) == 2


def max(list,n,k):
    #date intrare: list - lista, n - nr de elemente din list, k - nr intreg
    #date iesire: un nr intreg ce reprezinta al k-lea cel mai mare element
    #sortez lista descrescator, astfel rezultatul se va aflat pe pozitia k-1
    list.sort(reverse = True);
    return(list[k-1])
    
test()
#citesc n si k
n = int(input("n= "))
k = int(input("k= "))
#citesc sirul
arr = [int(x) for x in input().split()]
#afisez rezultatul
print(max(arr,n,k))