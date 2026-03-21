def construir_matriz_compras(lista_compras, n_clientes, m_produtos):    
    matriz_A = [[0]* m_produtos for _ in range(n_clientes)]  # Criamos uma matriz de zeros com n_clientes linhas e m_produtos colunas

    for i in range(n_clientes):
        for j in lista_compras[i]:
            matriz_A[i][j] = 1  # Marcamos com 1 onde o cliente i comprou o produto j

    return matriz_A



def construir_transposta(matriz_A, n_linhas, m_colunas):

    matriz_T= [[0]* n_linhas for _ in range(m_colunas)]  # Criamos uma matriz de zeros com m_colunas linhas e n_linhas colunas

    for i in range(n_linhas):
        for j in range(m_colunas):
            matriz_T[j][i] = matriz_A[i][j] # A transposta é obtida invertendo as posições de i e j


    return matriz_T


