def preencher_matriz():
    # Inicializa a matriz 4x4 com valores predefinidos
    MATRIZ = [
        [0, 1, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    # Preenche as posições não definidas com entrada do usuário
    for i in range(4):
        for j in range(4):
            if MATRIZ[i][j] == 0:  # Só pede input se o valor for 0
                while True:
                    try:
                        MATRIZ[i][j] = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
                        break  # Sai do loop se a entrada for válida
                    except ValueError:
                        print("Por favor, insira um número inteiro válido.")

    # Imprime a matriz de forma formatada
    print("\nMatriz preenchida:")
    for linha in MATRIZ:
        print(" ".join(f"{num:2}" for num in linha))

# Chama a função para executar
preencher_matriz()

 



