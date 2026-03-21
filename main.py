import csv

from similaridade import construir_matriz_compras, construir_transposta




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
        cliente = linha[1]
        produto = linha[2] 
        
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
        cliente = linha[1]
        produto = linha[2]
        
        # Pegamos os índices internos que criamos na primeira passagem
        id_cliente = mapa_clientes[cliente]
        id_produto = mapa_produtos[produto]
        
        # Adicionamos o id_produto na lista de compras do id_cliente
        # (Usando o set() aqui temporariamente só para não ter produto duplicado na lista)
        if id_produto not in lista_compras[id_cliente]:  #Se o produto ainda não estiver na lista de compras do cliente, adicionamos
            lista_compras[id_cliente].append(id_produto)


print(f"Total de Clientes: {len(vetor_clientes)}")
print(f"Total de Produtos Únicos: {len(vetor_produtos)}")






# ATIVIDADE 2: MÓDULO SIMILARIDADE

matriz_compras_A = construir_matriz_compras(lista_compras, len(vetor_clientes), len(vetor_produtos))
matriz_compras_T = construir_transposta(matriz_compras_A, len(vetor_clientes), len(vetor_produtos))