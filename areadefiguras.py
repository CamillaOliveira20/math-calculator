lado_quadrado = float(input("Qual o comprimento de um lado do quadrado? "))
area_quadrado = lado_quadrado*lado_quadrado
print(f"A área de um quadrado é: {area_quadrado} cm2 ou (area_quadrado/10000) m2")

comprimento_retangulo = float(input("Qual o comprimento do retângulo em cm? "))
largura_retangulo = float(input("Qual a largura do retângulo em cm? "))
area_retangulo = comprimento_retangulo * largura_retangulo
print(f"A área do retângulo é: {area_retangulo} cm2 ou (area_retangulo/10000) m2")


raio_circulo = float(input("Qual o comprimento do raio do circulo? "))
pi = 3.14
area_circulo= pi * raio_circulo**2
print(f"A area do circulo é: {area_circulo} m2 ou (area_circulo/10000) m2")