from os import system
from datetime import datetime
system('cls')

# Iniciando a classe Serviço
class Servico:
    # Construtor/Inicialize da classe
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco
        self.data = datetime.now().strftime('%d/%m/%Y')
        self.horario = datetime.now().strftime('%H:%M:%S')

    # Método para exibir os dados do serviço
    def exibir_dados(self):
        print(f'Data: {self.data}')
        print(f'Horário: {self.horario}')
        print(f'Descrição: {self.descricao}')
        print(f'Preço: R$ {self.preco:.2f}')
    # Método para salvar dados em TXT
    def salvar_historico(self):
        # Abre o arquivo em modo de escrita (append) para adicionar novos registros
        # utf-8 é usado para suportar caracteres especiais
        with open('historico_servicos.txt',"a", encoding='utf-8') as f:
            f.write(f'Data: {self.data}\n')
            f.write(f'Horário: {self.horario}\n')
            f.write(f'Descrição: {self.descricao}\n')
            f.write(f'Preço: R$ {self.preco:.2f}\n')
            f.write('-' * 40 + '\n')


# Iniciando o código principal
print(' == CADASTRO DE SERVIÇOS == ')

continuar = 'S'

while continuar.upper() != 'X':
    descricao = input('Informe a descrição do serviço: ')
    preco = input('Informe o preço do serviço: ')

    try:
        preco = float(preco)
    except ValueError:
        print('Preço inválido. Por favor, insira um número válido.')
        continue

    system('cls')
    # Criando uma instância da classe Serviço
    servico = Servico(descricao, preco)
    # Exibindo os dados do serviço
    servico.exibir_dados()
    # Salvar dados em arquivo TXT
    servico.salvar_historico()
    print('-' * 40)

    continuar = input('Tecle "Enter" para continuar ou "X" para sair: ')
    system('cls')
