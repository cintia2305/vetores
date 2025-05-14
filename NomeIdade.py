vetorDeIntereiros = [0] * 4

vetorDeIntereiros = [0] * 2

NOME = [0] * 3
IDADE = [0] * 3
TELEFONE = [0] * 3
RUA = [0] * 3
NUMERO = [0] * 3
BAIRRO = [0] * 3 

cont = 0
for cont in range(3):
    print(f"-----{cont + 1}º-CADASTRO------------")
    print()

    print("Digite o seu nome:")
    NOME[cont] = input()
    print("Digite a sua idade")
    IDADE[cont] = int(input())
    print("Digite o seu telefone")
    TELEFONE[cont] = int(input())
    print("digite a sua rua")
    RUA[cont] = int(input())
    print("digite o seu numero")
    NUMERO[cont] = int(input())
    print("digite o seu bairro")
    BAIRRO[cont] = int(input())
    
    print(f"----------------------")
    print(f"NOME: {NOME[cont]}")
    print(f"IDADE: {IDADE[cont]} anos")
    print(f"TELEFONE: {TELEFONE[cont]}")
    print(f"RUA: {RUA[cont]}")
    print(f"NUMERO: {NUMERO[cont]}")
    print(f"BAIRRO:  {BAIRRO[cont]}")
    print(f"-----------------------")