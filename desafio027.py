# Faça um programa que leoa o nome completo da pessoa, mostrando em seguida o primeiro e último nome separadamente.
# Ex.: Ana Maria de Souza
# primeiro = Ana
# último = Souza

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {0}.'.format(nome[0]))
print('Seu último nome é {0}.'.format(nome[len(nome) - 1]))