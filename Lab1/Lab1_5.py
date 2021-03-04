def test():
    assert f([1,2,3,3],4) == 3
    assert f([2,2,1],3) == 2
    assert f([1,1,2,3,4],5) == 1
def f(list,n):
    #date intrare: list - lista de elemente intregi, n - nr intreg ce reprezinta lungimea listei
    #date iesire: un nr intreg ce reprezinta nr care apare de doua ori in list
    #car este un vector caracteristic in care pe pozitia k voi avea nr de aparitii a lui k
    car = [0]*n;
    for i in range (0,n):
        #parcurg elemntele din list si verific daca el x a aparut pana acum, daca da il returnez, in caz contrar ii setez nr de
        #aparitii la 1
        if car[list[i]] == 0:
            car[list[i]] = 1
        elif car[list[i]] == 1:
            return list[i];
lst = [] 
test()
#citest n
n = int(input("Enter number of elements : "))
#citesc lista de elemente
lst = [int(x) for x in input().split()]
print("Nr este:")
#afisez rezultatul
print(f(lst,n))
