# 1
def primeiro_elemento(vet: list) -> int:
    return vet[0]

# 2
def exibe_negativos(vet: list) -> None:
    for i in range(5):
        if vet[i] < 0:
            print(f"v[{i}] = {vet[i]}")

# 3

def soma_elementos(vet: list) -> int:
    #soma = 0
    #for i in range(len(vet)):
    #    soma += vet[i]
    return sum(vet)

# 4

def media_vetor(vet: list) -> float:
    soma = 0
    for i in range(len(vet)):
        soma += vet[i]

    return (soma / len(vet))

# 5

def impares_vetor(vet: list) -> None:
    for i in range(len(vet)):
        if vet[i] % 2 == 1:
            print(f"v[{i}] = {vet[i]}")

# 6

def primeiro_ultimo(vet: list) -> None:
    print(f"O primeiro elemento do vetor é {vet[0]} e o último é {vet[len(vet) - 1]}")

# 7

def impares(vet: list) -> None:
    for i in range(len(vet)):
        if i % 2 == 1:
            print(str(vet[i]))

# 8

def verif_vetor(vet: list, num: float) -> bool:
    if num in vet:
        return True
    else:
        return False

# 9

def ordena_vetor(vet: list) -> None:
    print(f"""
    {sorted(vet)}
    """)

# 10

def copia_vetor(v1: list, v2:list) -> None:
    v2 = v1
    print(f"Vetor 1 - {str(v1)}")
    print(f"Vetor 2 - {str(v2)}")

# 11

def inverte_vetor(v1: list, v2:list) -> None:
    a = len(v1) - 1
    print(a)
    for b in range(len(v1)):
        print(str(v1[b]))
        v2[a] = v1[b]
        a -= 1
    print(f"Vetor 1 - {str(v1)}")
    print(f"Vetor 2 - {str(v2)}")

# 12

def ordena_vetor_crescente(vet:list) -> None:
    vet.sort()
    print(str(vet))

# 13

def ordena_vetor_decrescente(vet: list) -> None:
    vet.sort(reverse=True)
    print(str(vet))