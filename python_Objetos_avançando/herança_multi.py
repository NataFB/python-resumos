class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

#MIXIN: Elas são bastante utilizadas em Python no caso de precisarmos compartilhar algum comportamento que não é o mais importante desta classe. Igual utilizamos em Hipster:

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'
    
class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass



rubens = Senior('Rubens')
print(rubens)

#MRO:
#pleno => Alura => Funcionario => Caelum => Funcionario
# o MRO do python 3 remove o primeiro Funcionario porque não é uma "good head" ja que tem Caelum abaixo de Funcionarios para verificar primeiro
#assim fica a ordem nova: Pleno => Alura => Caelum => Funcionario
