lista_frutas = ['maçã', 'banana', 'pera']
print(lista_frutas[0])

# Imprimirá: 'maçã'

lista_frutas = ['maçã', 'banana', 'pera']
fruta_preferida = lista_frutas[2]

print(fruta_preferida)
print(lista_frutas)

# O primeiro print() imprimirá: 'pera'
# O segundo print() imprimirá: ['maçã', 'banana', 'pera']

lista_frutas = ['maçã', 'banana', 'pera']
# Em Python, a função len(), do inglês length (cumprimento), nos permite saber a quantidade de itens num array, basta passar o nome da variável que guarda o array como argumento.
quantidade_frutas = len(lista_frutas)

print(quantidade_frutas)

# Imprimirá o número 3, pois lista_frutas tem três elementos

lista_frutas = ['maçã', 'banana', 'pera']

print(len(lista_frutas))

# Também imprimirá o número 3

lista_frutas = ['maçã', 'banana', 'pera']

# O valor do índice de 'pera', o último elemento do array, é 2
# O valor do len(lista_frutas) é 3

# Percorrer arrays
lista_frutas = ['maçã', 'banana', 'pera']

for i in range(3):
    print(lista_frutas[i])

# Imprimirá:
# maçã
# banana
# pera

lista_num = [2, 45, 65, 78, 126, 987, 457,
             345, 679, 107, 2345, 452, 3, 34, 560]

for i in range(15):
    print(lista_num[i])

# Percorrer arrays com len()
lista_num = [2, 45, 65, 78, 126, 987, 457,
             345, 679, 107, 2345, 452, 3, 34, 560]

for i in range(len(lista_num)):
    print(lista_num[i])

# Alterar dados usando índices
lista_frutas = ['maçã', 'banana', 'pera']
print(lista_frutas)
# Imprimirá: ['maçã', 'banana', 'pera']

lista_frutas[0] = 'melancia'
print(lista_frutas)
# Imprimirá: ['melancia', 'banana', 'pera']

# Alterar dados usando indices
lista_frutas = ['melancia', 'banana', 'pera']
print(lista_frutas)
# Imprimirá: ['melancia', 'banana', 'pera']

lista_frutas[1], lista_frutas[2] = 'morango', 'abacaxi'
print(lista_frutas)
# Imprimirá: ['melancia', 'morango', 'abacaxi']

lista_frutas = ['melancia', 'morango', 'abacaxi']
print(lista_frutas)
# Imprimirá: ['melancia', 'morango', 'abacaxi']

lista_frutas[1] = lista_frutas[0]
print(lista_frutas)
# Imprimirá: ['melancia', 'melancia', 'abacaxi']

