# Calcular a area de um retangulo
# float = ponto flutuante, ou seja, aceita casas decimais
base = input('Digite a base do retângulo: ')
altura = input('Digite a altura do retângulo: ')

#  Valida se a Base e Altura são números
print('Base é numérico?', base.isnumeric())
print('Altura é numérico?', altura.isnumeric())

#Calcula a área do retângulo
area = float(base)*float(altura)

print('Base: {}, Altura {}, Área {}'. format(base, altura, area))
