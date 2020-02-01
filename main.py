import math
import linecache

i=1
case = 1
count = len(open('plik.txt', 'r').readlines())
while i<= count-1 :
    listaA = linecache.getline('plik.txt',i).split()
    listaB = linecache.getline('plik.txt',i+1).split()
    #print(listaA + listaB)
    dx = int(listaB[0]) - int(listaA[0])
    dy = int(listaB[1]) - int(listaA[1])
    dz = int(listaB[2]) - int(listaA[2])
    l = round(math.sqrt(math.pow(dx, 2) + math.pow(dy, 2) + math.pow(dz, 2)),3)
    print(str(case)+". l - distance between points A, B, rounded to 3 decimal places")
    print("A" + str(listaA) + " B" + str(listaB))
    print("l= " + str(l))
    #exporting results to file
    plik = open('wyniki.txt', 'a')
    plik.writelines("punkty: A" + str(listaA)+ " B" + str(listaB)+ "\n" )
    plik.writelines("l= "+str(l) + "\n" )
    plik.close()

    i=i+1
    case=case+1




