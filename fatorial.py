'''
Programa que lê um número inteiro n >= 0 e imprime n!
'''

print("Cálculo do fatorial de um número\n")

# leia o valor de n
n = int(input("Digite um número inteiro não-negativo: "))

i = 1  # contador
n_fat = 1 # variável de cálculo fatorial

# calcule n!
while i <= n:
    n_fat = n_fat * i
    i = i + 1
    print(i-1, "Fatorial =", n_fat)
