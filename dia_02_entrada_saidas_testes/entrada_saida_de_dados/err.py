# import sys


# err = "Arquivo não encontrado"
# print(f"Erro aconteceu: {err}", file=sys.stderr)
def sum() -> any:
    nums = input("Insira valores aqui, separados por espaço: ")

    nums_arr = nums.split(" ")

    sum = 0
    for num in nums_arr:
        if not num.isdigit():
            print(f"Erro ao somar valores, {num} não é um dígito.")
        else:
            sum += int(num)

    print(f"A soma dos valores válidos é: {sum}")


def return_interger():
    while True:
        try:
            x = int(input("Por favor digite um número inteiro: "))
            print(x)
            break
        except ValueError:
            # 'ValueError' é a exceção que ocorre quando a função int()
            #  recebe um valor que não pode ser traduzido para número inteiro
            print("Oops! Esse não era um número inteiro. Tente novamente...")


def read_file():
    try:
        with open("arquiv.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        # será executado caso haja a exceção 'FileNotFoundError'
        print("Arquivo inexistente")
    else:
        # será executado se tudo ocorrer bem no try
        print("Arquivo manipulado e fechado com sucesso")
    finally:
        # será sempre executado, independentemente de erro
        print("Fim da tentativa de ler o arquivo")
