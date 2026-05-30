# Calcula a soma de todos os preços:
def calcular_total(produtos):
    return sum(produtos.values())

# Encontra o produtos mais caro:
def produto_mais_caro(produtos):
    maior_preco = max(produtos.values())
    for nome, preco in produtos.items():
        if preco == maior_preco:
            return nome, maior_preco
        
# Encontra o produto mais barato:
def produto_mais_barato(produtos):
    menor_preco = min(produtos.values())
    for nome, preco in produtos.items():
        if preco == menor_preco:
            return nome, menor_preco
        
# Buscar produto pelo nome:
def exibir_produto(produtos, nome):
   return produtos.get(nome, "Produto não encontrado")

#Função princípal, adiciona os produtos e os valores e exibe os resultados. 
def main():  
    produtos = {}
    for i in range(5):
        nome = input('Digite o nome do produto: ')
        while True:
            try:
                inserir_valor = float(input('Digite o valor: '))
                break
            except ValueError:
                print("Valor inválido.")
        produtos[nome] = inserir_valor
    
    print('Os produtos são: ' , produtos)
    print('Valor total: R$', calcular_total(produtos))
    print('Produto mais caro: ', produto_mais_caro(produtos))
    print('Produto mais barato: ', produto_mais_barato(produtos))
    media = calcular_total(produtos) / len(produtos)
    print('A média dos produtos é: ', media)

    nome = input('Procure um produto: ')
    print(exibir_produto(produtos, nome))

if __name__ == "__main__":
    main()
