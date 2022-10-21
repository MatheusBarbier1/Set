mat = [[0 for i in range(3)]for j in range(3)] # Cria matriz
vet = [] # Vetor

# Roda a matriz
for i in range(3):
    for j in range(3):
        mat[i][j] = int(input("Valor? ")) # Insere os valores da matriz
        if i == j:
            vet.append(mat[i][j]) # Se o valor de i e j forem iguais ele adiciona o numero ao vetor


print(mat)
print()
print(vet)
