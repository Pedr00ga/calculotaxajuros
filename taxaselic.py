from datetime import datetime

def taxaano(valor, taxas, meses):
    juros_ano = taxas / 12
    juros_total = juros_ano * meses
    pt1 = (valor * (juros_total / 100))
    resultado = pt1 + valor
    print(f"O valor do juros é de R${round(pt1, 2)}")
    return round(resultado, 2)



resultado = taxaano(valor = float(input("Digite o valor a se pagar: ")),
taxas = float(input("Digite o valor da taxa legal: ")), meses = float(input("Digite o valor total de meses: ")))

hoje = datetime.now()

print(f"O valor com a taxa legal é de: R${resultado}")

input("Pressione ENTER para sair...")