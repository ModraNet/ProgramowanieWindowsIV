ciagbinarny = []
iledziur = 0
etap = 0
while True:
    klawisz = int(input()) 
    if klawisz!=0 and klawisz!=1:
        break
    elif etap==0 and klawisz==1:
        etap=1
    elif etap==1 and klawisz==0:
        etap=2
    elif etap==2 and klawisz==1:
        iledziur+=1
        etap=1
print("Wykryto ",iledziur," dziur binarnych." )