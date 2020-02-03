import math
import linecache

def countDistanceBetweenTwoPoint3d(Ax, Ay, Az, Bx, By, Bz):
    dx = Bx - Ax
    dy = By - Ay
    dz = Bz - Az
    l = round(math.sqrt(math.pow(dx, 2) + math.pow(dy, 2) + math.pow(dz, 2)), 3)
    return l


i = 1
case = 1
count = len(open('plik.txt', 'r').readlines())
plik = open('wyniki.txt', 'w')

while i <= count - 1:
    listaA = linecache.getline('plik.txt', i).split()
    listaB = linecache.getline('plik.txt', i + 1).split()
    l = countDistanceBetweenTwoPoint3d(
        int(listaA[0]),
        int(listaA[1]),
        int(listaA[2]),
        int(listaB[0]),
        int(listaB[1]),
        int(listaB[2]))
    print(str(case) + ". l - distance between points A, B, rounded to 3 decimal places")
    print("A" + str(listaA) + " B" + str(listaB))
    print("l= " + str(l))
    # exporting results to file
    plik.writelines("punkty: A" + str(listaA) + " B" + str(listaB) + "\n")
    plik.writelines("l= " + str(l) + "\n")
    i = i + 1
    case = case + 1
plik.close()
