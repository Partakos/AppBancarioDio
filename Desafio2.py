def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []


    for transacao in transacoes:

        if abs(transacao) > limite:

            transacoes_filtradas.append(transacao)

    return transacoes_filtradas


dados_entrada = input()


dados_transacoes, limite = dados_entrada.split("],")
dados_transacoes = dados_transacoes.strip("[]").replace(" ", "")
limite = float(limite.strip()) 

transacoes = [int(valor) for valor in dados_transacoes.split(",")]

resultado = filtrar_transacoes(transacoes, limite)

print(f"Transações: {resultado}")