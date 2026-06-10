totalPeso = 0
totalFaturamento = 0
for i in range(0, 9 + 1, 1):
    print("Pacote " + str(i + 1) + ":")
    while True:    #This simulates a Do Loop
        print("Escreva o Peso do Pacote:")
        peso = float(input())
        if peso <= 0:
            print("Erro! O peso deve ser maior que zero.")
        if peso > 0: break
    while True:    #This simulates a Do Loop
        print("Digite o destino (Nacional ou Internacional):")
        destino = input()
        if destino != "Nacional" and destino != "Internacional" and destino != "nacional" and destino != "internacional" and destino != "NACIONAL" and destino != "INTERNACIONAL":
            print("Destino inválido!")
        if destino == "Nacional" or destino == "Internacional" or destino == "nacional" or destino == "internacional" or destino == "NACIONAL" or destino == "INTERNACIONAL": break
    if peso <= 2:
        print("custo = 10")
        custo = 10
    else:
        if peso <= 10:
            print("custo = 20")
            custo = 20
        else:
            print("custo = 30")
            custo = 30
    if destino == "Internacional" or destino == "internacional" or destino == "INTERNACIONAL":
        custo = custo + custo * 0.2
    totalPeso = totalPeso + peso
    totalFaturamento = totalFaturamento + custo
    print("Frete calculado: R$ " + str(custo))
ticketMedio = totalFaturamento / 10
print("========== RESULTADO FINAL ==========")
print("Total de pacotes: 10")
print("Carga total acumulada: " + str(totalPeso) + " kg")
print("Faturamento bruto do lote: R$ " + str(totalFaturamento))
print("Ticket médio por pacote: R$ " + str(ticketMedio))
print("====================================")