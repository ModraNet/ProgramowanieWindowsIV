A = []
B = []
polecenie = []
print("Wpisywanie do zbioru A...")
while polecenie!="stop":
    A.append(int(input())) 
    polecenie=input("Czy chcesz zatrzymać wpisywanie? (Jeśli tak, wpisz stop)")
print("Wpisywanie do zbioru B...")
polecenie = ""
while polecenie!="stop":
    B.append(int(input())) 
    polecenie=input("Czy chcesz zatrzymać wpisywanie? (Jeśli tak, wpisz stop)")
print(A)
print(B)
zbiorA = set(A)
zbiorB = set(B)
print(zbiorA | zbiorB)
print(zbiorA - zbiorB)
print(zbiorA & zbiorB)
print(zbiorA ^ zbiorB)