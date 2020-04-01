import random
import numpy
x=int(input("Podaj długość: "))
y=x
tab1 = [[0 for x in range(x)] for y in range(y)]
tab2 = [[0 for x in range(x)] for y in range(y)]
wyn = [[0 for x in range(x)] for y in range(y)]
for a in range (x):
    for b in range (y):
        tab1[b][a]=random.randint(-10,10)
        tab2[b][a]=random.randint(-10,10)
print("Macierz nr 1:\n",numpy.matrix(tab1))
print("Macierz nr 2:\n",numpy.matrix(tab2))
for a in range (x):
    for b in range (y):
        wyn[b][a]=tab1[b][a]+tab2[b][a]
print("Suma:\n",numpy.matrix(wyn))
for a in range (x):
    for b in range (y):
        wyn[b][a]=tab1[b][a]-tab2[b][a]
print("Różnica:\n",numpy.matrix(wyn))
wyn=numpy.dot(tab1,tab2)
print("Iloczyn:\n",numpy.matrix(wyn))