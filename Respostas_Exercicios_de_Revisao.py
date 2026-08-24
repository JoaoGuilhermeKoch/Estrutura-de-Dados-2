perguntas_respostas = [
    {
        "pergunta": "Questão 1 - O que é uma estrutura de dados?",
        "resposta": "Uma estrutura de dados é uma maneira de organizar e armazenar informações, facilitando sua utilização, acesso e manipulação."
    },

    {
        "pergunta": "Questão 2 - Qual é a diferença entre uma variável e uma lista?",
        "resposta": "Uma variável aponta para um único objeto, enquanto uma lista possibilita armazenar e organizar vários elementos em sequência."
    },

    {
        "pergunta": "Questão 3 - Qual é o primeiro índice de uma lista em Python?",
        "resposta": "O primeiro índice de uma lista em Python é 0."
    },

    {
        "pergunta": """Questão 4 - Quantos elementos existem em:

valores = [10, 20, 30, 40, 50]

E qual é o maior índice válido?""",
        "resposta": "A lista possui cinco elementos, com índices que vão de 0 até 4. Portanto, o maior índice válido é 4."
    },

    {
        "pergunta": """Questão 5 - O que representa:

matriz[2][3]""",
        "resposta": "Refere-se ao elemento localizado na linha de índice 2 e coluna de índice 3. Para acessá-lo, a matriz deve possuir no mínimo três linhas e quatro colunas."
    },

    {
        "pergunta": "Questão 6 - Qual é a diferença entre uma lista e uma tupla?",
        "resposta": "A principal diferença é que listas podem ser modificadas depois de criadas, enquanto tuplas não podem ser alteradas."
    },

    {
        "pergunta": "Questão 7 - Para que serve um dicionário?",
        "resposta": "É utilizado para relacionar chaves e valores, facilitando a organização e representação de informações."
    },

    {
        "pergunta": "Questão 8 - Para que podemos utilizar uma dataclass?",
        "resposta": "Para representar entidades que possuem uma estrutura definida, com atributos e, quando necessário, comportamentos próprios."
    },

    {
        "pergunta": "Questão 9 - Por que podemos utilizar uma lista de objetos?",
        "resposta": "Para reunir diversas entidades que apresentam a mesma estrutura, como, por exemplo, vários alunos ou produtos."
    },

    {
        "pergunta": "Questão 10 - O que significa modelar um problema?",
        "resposta": "Serve para descobrir, separar e organizar os dados que são importantes para resolver determinado problema."
    },

    {
        "pergunta": """Questão 11 - Explique o conceito de abstração utilizando um exemplo de sistema computacional.""",
        "resposta": "Abstração consiste em considerar apenas as características importantes para solucionar um problema, deixando de lado informações que não são necessárias."
    },

    {
        "pergunta": """Questão 12 - Por que o código abaixo pode produzir um comportamento inesperado?

matriz = [[0] * 3] * 3""",
        "resposta": """Isso acontece porque as três linhas acabam apontando para a mesma lista. Dessa forma, uma alteração feita em uma delas também pode modificar as outras.

Uma forma correta de criar a matriz é:

matriz = [[0] * 3 for _ in range(3)]"""
    }
]

for item in perguntas_respostas:
    print("=" * 80)
    print(item["pergunta"])
    print()
    print("RESPOSTA:")
    print(item["resposta"])
    print("=" * 80)
    print()
