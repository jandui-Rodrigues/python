file = open("arquivo.txt", mode="w")
# ao abrir um arquivo para escrita,
#  um novo arquivo é criado mesmo que ele já exista, sobrescrevendo o antigo.
# Criamos um contexto, limitando o escopo onde o arquivo está aberto.
# O uso do "as" aqui é somente para atribuir o valor utilizado no contexto
# à variável file


def write_file():
    with open("arquivo.txt", "w") as file:
        # como estamos DENTRO do contexto,
        #  verificamos que o arquivo está ABERTO
        # através do atributo booleano 'closed' (file.closed = False)
        file.write("Maria 45\n")
        file.write("Miguel 33\n")
        print("Túlio 22", file=file)
        LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
        file.writelines(LINES)
        print(file.closed)

    # como estamos FORA do contexto,
    #  o arquivo está FECHADO (file.closed = True)
    print(file.closed)


def open_and_write_text_test(number_test):
    # escrita
    if number_test == 1:
        with open("arquivo.txt", "w") as file:
            file.write("Teste S2")

        # leitura
        with open("arquivo.txt", "r") as file:
            content = file.read()
            print(content)
    else:
        # escrita
        with open("arquivo.txt", "w") as file:
            LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
            file.writelines(LINES)

        # leitura
        with open("arquivo.txt", "r") as file:
            for line in file:
                print(line)
            # não esqueça que a quebra de linha também é um caractere da linha


def write_file_not_aproves(not_aproves):
    with open("notAproves.txt", "w") as file:
        file.writelines(not_aproves)


def check_status_student(students):
    list_not_aproves = []

    for student in students:
        name_student, note = student.split()
        if int(note) < 6:
            list_not_aproves.append(name_student + "\n")
    return list_not_aproves


def status_aprove():
    with open("notas.txt", "r") as file:
        content = file.read()
        students = content.split("\n")
    list_not_aproves = check_status_student(students)

    write_file_not_aproves(list_not_aproves)


status_aprove()
