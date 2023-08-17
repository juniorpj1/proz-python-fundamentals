prato_preferido = "xtudo"
bebida_preferida = "cerveja"
custo_prato = 25.0
custo_cerveja = 3.00
limite_gasto = 50.00

total_gasto = custo_prato + custo_cerveja
print("Total: : ", total_gasto)

troco = limite_gasto - total_gasto
print("Troco: ", troco)

if troco >= 0:
    print("Ainda tem dinheiro para comprar mais")
else:
    print("Não tem mais dinheiro para comprar mais")
