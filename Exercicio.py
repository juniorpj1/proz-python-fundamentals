# Entrada de dados
quantidade_rodas = int(input("Informe a quantidade de rodas do veículo: "))
peso_bruto = float(input("Informe o peso bruto do veículo em quilogramas: "))
quantidade_pessoas = int(input("Informe a quantidade de pessoas no veículo: "))

# Verificar categoria de habilitação
if quantidade_rodas == 2 or quantidade_rodas == 3:
    categoria = 'Categoria A'
elif quantidade_rodas == 4 and quantidade_pessoas <= 8 and peso_bruto <= 3500:
    categoria = 'Categoria B'
elif (quantidade_rodas == 4 or quantidade_rodas > 4) and 3500 < peso_bruto <= 6000:
    categoria = 'Categoria C'
elif (quantidade_rodas == 4 or quantidade_rodas > 4) and quantidade_pessoas > 8:
    categoria = 'Categoria D'
elif (quantidade_rodas == 4 or quantidade_rodas > 4) and peso_bruto > 6000:
    categoria = 'Categoria E'
else:
    categoria = 'Categoria não identificada'

# Exibir resultado
print(
    f"A melhor categoria de habilitação para o veículo informado é: {categoria}")
