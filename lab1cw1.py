i = True
elementy = []  
while i==True:
    elementy.append(input("Podaj element: "))
    print("Czy chcesz podać następny element? (0 - nie, 1 - tak)")
    i=int(input())
print("Wszystkich unikalnych elementów jest: ",len(set(elementy)))