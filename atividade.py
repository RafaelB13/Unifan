# Define o tamanho da tabela hash   
TAMANHO = 15

# Classe que representa o Livro
class Livro:
    def __init__(self, titulo, autor, identificacao):
        self.titulo = titulo
        self.autor = autor
        self.identificacao = identificacao

# Função que calcula o fator Hash
def funcao_hash(chave):
    return chave % TAMANHO

# Função que insere um valor na tabela hash
def inserir_hash(tabela, livro):
    indice = funcao_hash(livro.identificacao)
    posicao = indice

    while tabela[posicao] is not None:
        posicao = (posicao + 1) % len(tabela)
        if posicao == indice:
            print("A tabela hash está cheia. Redimensionamento necessário.")
            return

    tabela[posicao] = livro

# Função para buscar um valor na tabela Hash
def buscar(table, identificacao):
    # A função funcao_hash é utilizada para calcular 
    # o índice na tabela hash onde o livro com a chave 
    # identificacao deve estar armazenado.
    indice = funcao_hash(identificacao)

    # Verifica se houve uma colisão e que a lista 
    # contém os livros que colidiram.
    if isinstance(table[indice], list):
        for livro in table[indice]:
            # Compara a chave do livro com a chave que está sendo buscada.
            if livro.identificacao == identificacao:
                return livro
    elif table[indice] is not None:
        if table[indice].identificacao == identificacao:
            return table[indice]
    return None

# Imprime os livros com uma visualização melhor
def imprimir_livros(tabela):
    print("Índice | Título               | Autor    | Identificação")
    print("-" * 60)
    for indice, livros in enumerate(tabela):
        if livros is None:
            print(f"{indice:<7} | {'':<20} | {'':<8} | {'':<13}")
        elif isinstance(livros, Livro):
            print(f"{indice:<7} | {livros.titulo:<20} | {livros.autor:<8} | {livros.identificacao:<13}")
        else:
            for livro in livros:
                print(f"{indice:<7} | {livro.titulo:<20} | {livro.autor:<8} | {livro.identificacao:<13}")
    print("-" * 60)
    
def popular_tabela(tabela):
    livros = [
        Livro("Livro 1", "Autor 1", 3910233),
        Livro("Livro 2", "Autor 2", 4401292),
        Livro("Livro 3", "Autor 3", 4401293),
        Livro("Livro 4", "Autor 3", 4401223),
        Livro("Livro 5", "Autor 5", 1210100),
        Livro("Livro 6", "Autor 6", 3910236),
        Livro("Livro 7", "Autor 7", 4401297),
        Livro("Livro 8", "Autor 8", 4401298),
        Livro("Livro 9", "Autor 9", 4401299),
        Livro("Livro 10", "Autor 10", 2101100)
    ]

    for livro in livros:
        inserir_hash(tabela, livro)

def main():
    tabela_hash = [None] * TAMANHO

    popular_tabela(tabela_hash)

    while True:
        print("\nSelecione uma opção:")
        print("  1 - Inserir")
        print("  2 - Buscar")
        print("  3 - Imprimir")
        print("  0 - Sair")

        option = input("\nInsira a opção: ")

        if option == "0":
            print("Saindo...")
            break
        elif option == "1":
            print("Opção 1 selecionada: Inserir\n")
            nome = input("Insira o título do livro: ")
            autor = input("Insira o nome do autor do livro: ")
            identificacao = int(input("Insira o identificação: "))

            if nome and autor and identificacao:
                inserir_hash(tabela_hash, Livro(nome, autor, identificacao))
                print("Livro inserido\n")
            else:
                print("Verifique os campos digitados\n")
        elif option == "2":
            print("Opção 2 selecionada: Buscar\n")
            identificacao = int(input("Insira o ID que deseja buscar: "))

            livro = buscar(tabela_hash, identificacao)
            if livro:
                print("Título           | Autor    | Identificação")
                print("-" * 45)
                print(f"{livro.titulo:<16} | {livro.autor:<8} | {livro.identificacao:<13}")
                print("-" * 45)
            else:
                print("\nLivro não encontrado\n")
        elif option == "3":
            print("Opção 3 selecionada: Imprimir\n")
            imprimir_livros(tabela_hash)
        else:
            print("Opção inválida. Por favor, selecione novamente.")

if __name__ == "__main__":
    main()
