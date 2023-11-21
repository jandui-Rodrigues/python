a, b = "cd"
print(a)  # saída: c
print(b)  # saída: d

head, *tail = (
    1,
    2,
    3,
)
# Quando um * está presente no desempacotamento,
#  os valores são desempacotados em formato de lista.
print(head)  # saída: 1
print(tail)  # saída: [2, 3]

fruta, *frutas = ['melao', 'melancia', 'uva']

print(fruta, frutas)

first_letter, *letters = 'palavras'

print(first_letter.upper() + ''.join(letters))

nome_e_nascimento = [("Felps", "México"), ("João", "Brasil")]
for nome, pais in nome_e_nascimento:
    print(nome, pais)
