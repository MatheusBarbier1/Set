# Verifica os tamanhos e mostra a quantidade de numeros repetidos
def func():
    x = len(set(vet))
    y = len(vet)
    result = y - x
    print(result)

vet = [] # vetor

# Roda vetor
for i in range(5):
    vet.append(int(input("Valor? ")))
func()