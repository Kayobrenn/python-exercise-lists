def coletar_dados():
    alturas = []
    generos = []
    
    for i in range(15):
        altura = float(input(f"Digite a altura da pessoa {i+1}: "))
        genero = input(f"Digite o gênero da pessoa {i+1} (Masculino ou Feminino): ").strip().lower()
        
        alturas.append(altura)
        generos.append(genero)
    
    return alturas, generos


def calcular_maior_menor_altura(alturas):
    maior_altura = max(alturas)
    menor_altura = min(alturas)
    return maior_altura, menor_altura


def calcular_media_masculino(alturas, generos):
    masculino_alturas = [alturas[i] for i in range(15) if generos[i] == 'masculino']
    if masculino_alturas:
        media_masculino = sum(masculino_alturas) / len(masculino_alturas)
    else:
        media_masculino = 0
    return media_masculino


def contar_feminino(generos):
    return generos.count('feminino')


def main():
    
    alturas, generos = coletar_dados()
    maior_altura, menor_altura = calcular_maior_menor_altura(alturas)
    media_masculino = calcular_media_masculino(alturas, generos)
    numero_feminino = contar_feminino(generos)
    
    
    print(f"\nMaior altura do grupo: {maior_altura} metros")
    print(f"Menor altura do grupo: {menor_altura} metros")
    print(f"Média de altura do gênero Masculino: {media_masculino:.2f} metros")
    print(f"Número de pessoas do gênero Feminino: {numero_feminino}")

if __name__ == "__main__":
    main()

alturas = []
