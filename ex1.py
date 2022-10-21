mat = [[0 for i in range(3)]for j in range(3)] # Cria a matriz


# Roda a matriz
for i in range(3):
    for j in range(3):
        mat[i][j] = int(input("Valor? "))

# faz os determinantes
detpos = mat[0][0] * mat[1][1] * mat[2][2] + mat[0][1] * mat[1][2] * mat[2][0] + mat[0][2] * mat[1][0] * mat[2][1]
det_neg = mat[2][0] * mat[1][1] * mat[0][2] - mat[2][1] * mat[1][2] * mat[0][0] + mat[2][2] - mat[1][0] * mat[0][1]

# Resultado
det = detpos - det_neg

print(det)