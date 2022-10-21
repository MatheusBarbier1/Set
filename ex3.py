# Funcao transformando os numeros e printando
def binario():
    for i in range(30):
        if vet[i] >= 0:
            vet[i] = 1
        else:
            vet[i] = 0
    print(vet)

vet = [] # Cria vetor

# Roda o vetor
for i in range(30):
    vet.append(int(input("Qual o valor? ")))

binario()