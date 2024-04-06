from subalgoritmos import *

v = [45, -89, 32, -12, 33]
v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

import os
while True:
    os.system("cls")
    print(""" 
    0. Sair
    1. Primeiro elemento do vetor. 
    2. Exiba somente os números negativos contidos no vetor.
    3. Soma dos elementos do vetor
    4. Média dos elementos do vetos
    5. Numeros ímpares contidos no vetor
    6. Exibe o primeiro e último elemento do vetor
    7. Exibe os números com índices impares
    8. Verifica se um valor está no vetor
    9. Ordena os elementos do vetor
    10. Copia os elementos do vetor v1 no vetor v2
    11. Copia os elementos do vetor v1 invertidos no vetor v2
    12. Ordena o vetor de forma crescente
    13. Ordena o vetor de forma decrescente
    14. Ordena vetor de forma crescente ou decrescente
    """)
    opcao = input("Escolha: ")
    if not opcao.isnumeric():
        input("Opção inválida!\nPressione alguma tecla para continuar . . .")
        continue
    opcao = int(opcao)
    match opcao:
        case 0:
            break

        case 1:
            print(f"Primeiro elemento: {primeiro_elemento(v)}")

        case 2:
            exibe_negativos(v)

        case 3:
            print(f"A soma dos elementos do vetor é {soma_elementos(v)}")

        case 4:
            print(f"A média dos elementos do vetor é {media_vetor((v))}")

        case 5:
            impares_vetor(v)

        case 6:
            primeiro_ultimo(v)

        case 7:
            impares(v)

        case 8:
            num = float(input("Digite um valor para ser comparado com o vetor: "))
            if verif_vetor(v, num) == True:
                print("O valor está no vetor v.")
            else:
                print("O valor não está no vetor v.")

        case 9:
            ordena_vetor(v)

        case 10:
            copia_vetor(v1, v2)

        case 11:
            inverte_vetor(v1, v2)

        case 12:
            while True:
                opcao = int(input("Digite o vetor para ser ordenado (1 = v1, 2 = v2): "))
                match opcao:
                    case 1:
                        ordena_vetor_crescente(v1)
                        break
                    case 2:
                        ordena_vetor_crescente(v2)
                        break
                    case _:
                        print("Digite uma opção válida (1 ou 2)")

        case 13:
            while True:
                opcao = int(input("Digite o vetor para ser ordenado (1 = v1, 2 = v2): "))
                match opcao:
                    case 1:
                        ordena_vetor_decrescente(v1)
                        break
                    case 2:
                        ordena_vetor_decrescente(v2)
                        break
                    case _:
                        print("Digite uma opção válida (1 ou 2)")

    input("Digite algo para continuar . . .")
            