def calcular_media(numeros):
    if not numeros:
        return 0
    soma = sum(numeros)
    media = soma / len(numeros)
    return media


# Teste da função
numeros = [10, 20, 30, 40, 50]
media_calculada = calcular_media(numeros)

print(f"A média é: {media_calculada}")

if media_calculada >= 30:
    print(f"Parabéns! Você passou com média {media_calculada} pontos!")
else:
    print(f"Infelizmente, você não atingiu a média necessária.")

