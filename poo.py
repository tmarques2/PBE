class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao, disponivel = True):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel
    def emprestar(self):
        if not self.disponivel:
            raise Exception ("Livro não disponível")
        self.disponivel = False
    def devolver(self):
        if self.disponivel:
            raise Exception ("Livro já devolvido")
        self.disponivel = True
    def obter_info(self):
        status = "Sim" if self.disponivel else "Não"
        return f"Título: {self.titulo}, Ano: {self.ano_publicacao}, Disponível: {status}"

'''livro = ItemBiblioteca("Dom Quixote", 1605)
print(livro.obter_info())
livro.emprestar()
print(livro.obter_info())
livro.devolver()
print(livro.obter_info())'''

class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel=True):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.livros = []
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    def verificar_disponibilidade_colecao(self):
        return all(livro.disponivel for livro in self.livros)
    def obter_info(self):
        status_colecao = "Sim" if self.verificar_disponibilidade_colecao() else "Não"
        titulos = ", ".join([livro.titulo for livro in self.livros]) if self.livros else "Nenhum livro na coleção"
        return (f"Título da Coleção: {self.titulo}, Ano: {self.ano_publicacao}, "
                f"Todos disponíveis: {status_colecao}\nLivros na coleção: {titulos}")

'''livro1 = ItemBiblioteca("Crepúsculo", 2005)
livro2 = ItemBiblioteca("Lua Nova", 2006)
livro3 = ItemBiblioteca("Eclipse", 2007)
livro4 = ItemBiblioteca("Amanhecer", 2008)

trilogia = ColecaoLivros("Crepúsculo", 2008)

trilogia.adicionar_livro(livro1)
trilogia.adicionar_livro(livro2)
trilogia.adicionar_livro(livro3)
trilogia.adicionar_livro(livro4)

print(trilogia.obter_info())

livro3.emprestar()

print(trilogia.obter_info()) '''

class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, numero_edicao, disponivel = True):
        super().__init__(titulo, ano_publicacao)
        self.numero_edicao = numero_edicao
    def atualizar_edicao(self, nova_edicao):
        if nova_edicao <= 0:
            raise ValueError("Número da edição deve ser maior que 0.")
        self.numero_edicao = nova_edicao
    def restringir_emprestimo(self, dias_max):
        if self.ano_publicacao < 2000:
            return dias_max <= 7
        else:
            return dias_max
    def obter_info(self):
        status = "Sim" if self.disponivel else "Não"
        return (f"Título: {self.titulo}, Ano: {self.ano_publicacao}, "
                f"Edição: {self.numero_edicao}, Disponível: {status}")
    
'''revista1 = Revista("Revista Ciência", 1995, 10)
print(revista1.obter_info())
print(revista1.restringir_emprestimo(5))
print(revista1.restringir_emprestimo(10))

revista1.atualizar_edicao(12)
print(revista1.obter_info())'''

class Biblioteca:
    def __init__(self):
        self.itens = {}
    def adicionar_item(self, item):
        self.itens[item.titulo] = item
    def remover_item(self, titulo):
        del self.itens[titulo]
    def listar_itens_disponiveis(self):
        return [titulo for titulo, item in self.itens.items() if item.disponivel]
    def contar_itens_emprestados(self):
        return sum(1 for item in self.itens.values() if not item.disponivel)
    
'''livro = ItemBiblioteca("Dom Quixote", 1605)
revista = Revista("Revista Ciência", 1995, 10)

biblioteca = Biblioteca()
biblioteca.adicionar_item(livro)
biblioteca.adicionar_item(revista)

print("Itens disponíveis na biblioteca:")
for titulo in biblioteca.listar_itens_disponiveis():
    print(f" - {titulo}")

livro.emprestar()

print("Itens disponíveis na biblioteca:")
for titulo in biblioteca.listar_itens_disponiveis():
    print(f" - {titulo}")

print(f"\nNúmero de itens emprestados: {biblioteca.contar_itens_emprestados()}")

biblioteca.remover_item("Dom Quixote")

print("Itens disponíveis na biblioteca:")
for titulo in biblioteca.listar_itens_disponiveis():
    print(f" - {titulo}")'''

class RelatorioBiblioteca(Biblioteca):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
    def gerar_relatorio_completo(self):
        return "\n".join(item.obter_info() for item in self.biblioteca.itens.values())
    def gerar_relatorio_disponibilidade(self):
        disponiveis = self.biblioteca.listar_itens_disponiveis()
        return f"Itens disponíveis ({len(disponiveis)}):\n - " + "\n - ".join(disponiveis)
    def gerar_relatorio_emprestimos(self):
        total = len(self.biblioteca.itens)
        emprestados = self.biblioteca.contar_itens_emprestados()
        proporcao = (emprestados / total * 100) if total else 0
        return (f"Número de itens emprestados: {emprestados}\n"
                f"Proporção de itens emprestados: {proporcao:.2f}%")
    
biblioteca = Biblioteca()

livro = ItemBiblioteca("Dom Quixote", 1605)
revista = Revista("Revista Ciência", 1995, 10)

biblioteca.adicionar_item(livro)
biblioteca.adicionar_item(revista)

livro.emprestar()

relatorio = RelatorioBiblioteca(biblioteca)

print("=== Relatório Completo ===")
print(relatorio.gerar_relatorio_completo())

print("\n=== Relatório de Disponibilidade ===")
print(relatorio.gerar_relatorio_disponibilidade())

print("\n=== Relatório de Empréstimos ===")
print(relatorio.gerar_relatorio_emprestimos())
