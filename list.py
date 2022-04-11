

lista = []
suma = 0

for i in range(0,10):
    nota = int(input("notas: "))
    lista.append(nota)
    suma += nota
    print(nota)
    

formula = suma / 10
print(formula)
if formula > 70:
    print("aprobaste")
else:
    print("prende la camara")
    
