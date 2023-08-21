# Usando a função range() para criar uma lista de números
for andar in range(1, 21):
    if andar != 13:
        print(andar)

# Usando a função while para criar uma lista de números
andar = 1
while andar <= 20:
    if andar != 13:
        print(andar)
    andar += 1

# Usando a função while true (do while) para resolver o problema
andar = 1
while True:
    if andar != 13:
        print(andar)
    andar += 1
    if andar > 20:
        break
