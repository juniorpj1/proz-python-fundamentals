# Imprima todos os números exceto 13 (laço 'for in range')

for andar in range(1, 21):
    if andar == 13:
        continue
    else:
        print(andar)

# Imprimir todos os números exceto 13 (laço 'while')

andar = 1
while andar <= 20:
    if andar == 13:
        andar += 1
        continue
    else:
        print(andar)
        andar += 1

# Imprimir tdos os números exceto 13 em ordem descrescente (laço 'while true')

for i in range(20, 0, -1):
    if i == 13:
        continue
    else:
        print(i)
