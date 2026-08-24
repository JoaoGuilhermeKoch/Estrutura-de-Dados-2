class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


# Lista de 5 produtos
produtos = [
    Produto("Televisão", 8500.00, 17),
    Produto("Monitor", 2649.00, 19),
    Produto("Fonte", 449.00, 21),
    Produto("PC", 7200.00, 8),
    Produto("Gabinete", 299.00, 33)
]


# Cálculo do valor total em estoque
valor_total = sum(
    produto.preco * produto.quantidade
    for produto in produtos
)


# Produto mais caro
produto_mais_caro = max(
    produtos,
    key=lambda produto: produto.preco
)


# Produto com maior quantidade armazenada
produto_maior_quantidade = max(
    produtos,
    key=lambda produto: produto.quantidade
)


# Resultados
print(f"Valor total em estoque: R$ {valor_total:.2f}")

print(
    f"Produto mais caro: {produto_mais_caro.nome} "
    f"- R$ {produto_mais_caro.preco:.2f}"
)

print(
    f"Produto com maior volume armazenado: "
    f"{produto_maior_quantidade.nome} "
    f"- {produto_maior_quantidade.quantidade} unidades"
)
