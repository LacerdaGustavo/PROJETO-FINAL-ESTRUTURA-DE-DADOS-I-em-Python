import csv

from similaridade import construir_matriz_compras, construir_transposta, multiplicar_matrizes, calcular_matriz_similaridade


# ATIVIDADE 1: MÓDULO LISTA DE COMPRAS

vetor_clientes = []       # Índice interno -> Código do cliente              (Seria em C++ std::vector)
mapa_clientes = {}        # Código do cliente -> Índice interno              (Seria em C++ std::map)

#mapa_clientes usa tabela hash para acessar o índice interno do cliente, o que torna a busca muito rápida (O(1)

vetor_produtos = []       # Índice interno -> Nome (ou código) do produto
mapa_produtos = {}        # Código do produto -> Índice interno

lista_compras = []        # Vetor onde cada posição (cliente) tem uma lista de produtos


# PRIMEIRA PASSAGEM
with open("dados_venda_cluster_20.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # Pula o cabeçalho
    
    for linha in leitor:
        cliente = linha[1].strip()
        produto = linha[2].strip()
        
        # 1. Se o cliente ainda não está no mapa, adicionamos ele
        if cliente not in mapa_clientes:
            indice_novo_cliente = len(vetor_clientes) # O tamanho atual vira o índice
            mapa_clientes[cliente] = indice_novo_cliente
            vetor_clientes.append(cliente)    # O cliente é adicionado no vetor na posição do índice
            
            # Já preparamos a lista de compras dele vazia na mesma posição!
            lista_compras.append([])
            
        # 2. Se o produto ainda não está no mapa, adicionamos ele
        if produto not in mapa_produtos:
            indice_novo_produto = len(vetor_produtos)
            mapa_produtos[produto] = indice_novo_produto
            vetor_produtos.append(produto)


# SEGUNDA PASSAGEM
with open("dados_venda_cluster_20.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)
    
    for linha in leitor:
        cliente = linha[1].strip()
        produto = linha[2].strip()
        
        # Pegamos os índices internos que criamos na primeira passagem
        id_cliente = mapa_clientes[cliente]
        id_produto = mapa_produtos[produto]
        
        # Adicionamos o id_produto na lista de compras do id_cliente
        # (Usando o set() aqui temporariamente só para não ter produto duplicado na lista)
        if id_produto not in lista_compras[id_cliente]:  #Se o produto ainda não estiver na lista de compras do cliente, adicionamos
            lista_compras[id_cliente].append(id_produto)


# 👉 CORREÇÃO APLICADA AQUI: Este bloco inteiro foi puxado para a margem esquerda para sair do loop acima
# testador da atividade 1 que vai imprimir os clientes e os produtos que compraram, usando os codigos originais
print("\nTESTADOR DA ATIVIDADE 1")
clientes_teste = ["99D7GX01", "53402701", "08912501"]
for codigo_original in clientes_teste:
    if codigo_original in mapa_clientes:
        indice_cliente = mapa_clientes[codigo_original]
        produtos_comprados = lista_compras[indice_cliente]
        print (f"Cliente {codigo_original} comprou {len(produtos_comprados)} produtos")
        for id_produto in produtos_comprados:
            codigo_produto = vetor_produtos[id_produto]
            print (f" Produto código: {codigo_produto}")
    else:
        print (f"Cliente {codigo_original} não encontrado")
print("-" * 30)


# ATIVIDADE 2: MÓDULO SIMILARIDADE

matriz_compras_A = construir_matriz_compras(lista_compras, len(vetor_clientes), len(vetor_produtos))
matriz_compras_T = construir_transposta(matriz_compras_A, len(vetor_clientes), len(vetor_produtos))
matriz_intersecao_I = multiplicar_matrizes(matriz_compras_A, matriz_compras_T, len(vetor_clientes), len(vetor_produtos))
matriz_similaridade_S = calcular_matriz_similaridade(matriz_intersecao_I, lista_compras, len(vetor_clientes))


# testador da atividade 2 que vai imprimir a similaridade entre os clientes, usando os codigos originais
print ("\nTESTADO DA ATIVIDADE 2")
clientes_teste = ["99D7GX01", "53402701", "08912501"]

for codigo_original in clientes_teste:
    if codigo_original in mapa_clientes:
        indice_cliente = mapa_clientes[codigo_original]

        menor_distancia = 2.0
        cliente_mais_similar = -1
        
        for j in range(len(vetor_clientes)):
            if j != indice_cliente and matriz_similaridade_S[indice_cliente][j] < menor_distancia: # Não comparamos o cliente com ele mesmo
                menor_distancia = matriz_similaridade_S[indice_cliente][j] # Atualiza o novo recorde
                cliente_mais_similar = j # Salva quem bateu o recorde
        
        # depois que o 'for' acabar de avaliar todo mundo, imprime SÓ o vencedor
        if cliente_mais_similar != -1:
            codigo_outro_cliente = vetor_clientes[cliente_mais_similar]