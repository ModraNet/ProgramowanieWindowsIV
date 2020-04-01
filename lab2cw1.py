import random
import math
wartosci=[2,3,3.5,4,4.5,5]
dltab=int(input("Podaj dlugosc tablicy: "))
tab=[]
for x in range(dltab):
    tab.append(wartosci[random.randint(0,5)])
print("Tablica:",tab)
srednia=0 
mini=5 
maks=2 
odch=0
for x in range(dltab):
    srednia=srednia+tab[x]
    if mini>tab[x]:
        mini=tab[x]
    if maks<tab[x]:
        maks=tab[x]
srednia=srednia/dltab
print("Srednia:",srednia)
print("Wartosci wieksze od sredniej: ")
for x in range(dltab):
    if(tab[x]>srednia):
        print(tab[x])
print("Wartosci mniejsze od sredniej: ")
for x in range(dltab):
    if(tab[x]<srednia):
        print(tab[x])
print("Min: ",mini)
print("Max: ",maks)
for x in range(dltab):
    odch=odch+math.pow((tab[x]-srednia),2)
odch=math.sqrt(odch/dltab)
print("Odchylenie standardowe: ",odch)