def test():
    assert distanta([1, 5], [4, 1]) == 5
    assert distanta([1, 1], [1, 1]) == 0


def distanta(p1, p2):
    #input: p1,p2 liste de 2 componente ( reprezinta cele 2 puncte)
    #output: distanta dintre ele
    #folosesc formula
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
test()
p1 = [0] * 2
p2 = [0] * 2
p1[0] = int(input("x1: "))
p1[1] = int(input("y1: "))
p2[0] = int(input("x2: "))
p2[1] = int(input("y2: "))

print(distanta(p1,p2))