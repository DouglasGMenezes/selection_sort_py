# # SELECTION SORT


class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome} - {self.idade} anos - CPF: {self.cpf}"

###############################

class Nodo:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None

###############################


class SelectionSort:
    def __init__(self):
        self.inicio = None

    def inserir(self, pessoa):
        novo = Nodo(pessoa)
        if not self.inicio:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.pessoa)
            atual = atual.proximo

    def contar_nodos(self):
        count = 0
        atual = self.inicio
        while atual:
            count += 1
            atual = atual.proximo
        return count

    def get_nodo_por_indice(self, index):
        atual = self.inicio

        for _ in range(index):
            if atual is None:
                return None
            atual = atual.proximo
        return atual


    def ordenar_por_idade(self):
        tamanho = self.contar_nodos()

        for i in range(tamanho):
            min_index = i
            nodo_min = self.get_nodo_por_indice(i)

            for j in range(i + 1, tamanho):
                nodo_j = self.get_nodo_por_indice(j)
                if nodo_j.pessoa.idade < nodo_min.pessoa.idade:
                    nodo_min = nodo_j
                    min_index = j

            nodo_i = self.get_nodo_por_indice(i)
            nodo_i.pessoa, nodo_min.pessoa = nodo_min.pessoa, nodo_i.pessoa



if __name__ == "__main__":
    lista = SelectionSort()

    lista.inserir(Pessoa("Alice", 30, "111.111.111-11"))
    lista.inserir(Pessoa("Bruno", 25, "222.222.222-22"))
    lista.inserir(Pessoa("Carla", 28, "333.333.333-33"))
    lista.inserir(Pessoa("Joao", 18, "444.444.444-44"))

    print("Antes:")
    lista.exibir()

    lista.ordenar_por_idade()

    print("\nDepois por idade:")
    lista.exibir()



