''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def calcular_saldo(transacoes):
    saldo = 0


    for transacao in transacoes:
        saldo += transacao


    return f"Saldo: R$ {saldo:.2f}"

dados_entrada = input()

dados_entrada = dados_entrada.strip("[]").replace(" ", "")
transacoes = [float(valor) for valor in dados_entrada.split(",")]

resultado = calcular_saldo(transacoes)


print(resultado)
