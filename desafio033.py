# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor deles.

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num3 and num2 > num1:
    maior = num2
else:
    maior =num3

if num1< num2 and num1 < num3:
    menor = num1
elif num2 < num3 and num2 < num1:
    menor = num2
else:
    menor = num3

print('O menor número é {0}.'.format(menor))
print('O maior número é {0}.'.format(maior))
