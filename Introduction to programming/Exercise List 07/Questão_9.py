# Desenho de Padrões com Caracteres:
# Crie um programa que desenhe padrões simples com caracteres, como triângulos, quadrados ou losangos. 
# Utilize loops aninhados para controlar a quantidade de linhas e colunas e a exibição dos caracteres.

def desenhar_quadrado(n):
    for i in range(n):
        print('|' * n)

tamanho = int(input("Digite o tamanho do quadrado: "))
desenhar_quadrado(tamanho)