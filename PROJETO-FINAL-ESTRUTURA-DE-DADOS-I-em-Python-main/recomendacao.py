def gerar_recomendacoes (cliente_alvo, matriz_similaridade_S, lista_compras, m_produtos, n_clientes, k_recomendacoes=5):

    #identificação de vizinhos mais similares
    vizinhos = []
    for j in range (n_clientes):
        if j != cliente_alvo and matriz_similaridade_S[cliente_alvo][j] < 1.0: #1.0 é zero similaridade
            vizinhos.append(j)

    vetor_R = [1.0] * m_produtos
    produtos_comprados_alvo = lista_compras[cliente_alvo] #vai atras do que o cliente alvo ja comprou, para n recomendar prduto repetido

    #calculo do ranqueamento
    for s in vizinhos:
        distancia_s = matriz_similaridade_S[cliente_alvo][s]

        for p in lista_compras[s]: #para cada produto comprado pelo vizinho s
            if p not in produtos_comprados_alvo:
                vetor_R[p] = vetor_R[p] * distancia_s #aqui a gente vai multiplicando as distancias dos vizinhos que compraram o produto, para ranquear melhor os produtos que foram comprados por vizinhos mais proximos

    #ordenação e seleção
    produtos_para_ordenar = []
    for p in range(m_produtos):
        if vetor_R[p] < 1.0: #se o produto tiver sido comprado por algum vizinho, ele vai ter um valor menor que 1.0, e ai a gente adiciona ele na lista de produtos para ordenar
            produtos_para_ordenar.append((p, vetor_R[p]))

    def criterio_ordenacao(item):
        return item[1] #ordena pelo valor do vetor_R e ele é o segundo na tupla q tem acima
    
    produtos_para_ordenar.sort(key=criterio_ordenacao) #dos mais recomendados para os menos recomendados

    return produtos_para_ordenar[:k_recomendacoes] #retorna os k primeiros produtos recomendados, ou seja, os mais recomendados