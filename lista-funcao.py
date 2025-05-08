'''
#ex1
def calcular_dobro(precos):
    for produto in precos:
        dobro = produto * 2
        print(f"O dobro de {produto} é: {dobro}")

precos = [5.00, 8.00, 12.00]

calcular_dobro(precos)
'''
'''
#ex2
def boas_vindas(alunos):
    print("Bem-vindos ao curso online!")
    for aluno in alunos:
        print(f"Olá, {aluno}! Estamos felizes por ter você conosco.")

alunos = ["João", "Maria", "Carlos"]

boas_vindas(alunos)
'''
'''
#ex4
def verificar_numeros(numeros):
    for n in numeros:
        if n % 2 == 0:
            print(f"{n} é par. Avançar!")
        else:
            print(f"{n} é ímpar. Recuar!")

numeros = [4, 7, 10]

verificar_numeros(numeros)
'''
'''
#ex5
def tabuada(numeros):
    for n in numeros:
        print(f"\nTabuada do {n}")
        for i in range(1, 11):
            resultado = n * i
            print(f"{n} x {i} = {resultado}")

numeros = [2, 3, 4]

tabuada(numeros)
'''
'''
#ex6
def verificar_idade(clientes):
    for idade in clientes:
        if idade >=18:
            print(f"{idade} anos, pode assistir o filme")
        else:
            print(f"{idade} anos, não pode assistir o filme")

clientes = [15, 20, 8]

verificar_idade(clientes)
'''
'''
#ex7
def calcular_desconto(produtos):
    for preco in produtos:
        desconto = preco * 0.1
        preco_final = preco - desconto
        print(f"O preço é {preco}, com o desconto de 10% fica: {preco_final}")

produtos = [50.00, 120.00, 200.00]

calcular_desconto(produtos)
'''
'''
#ex8
def contar_letras(palavras):
    for l in palavras:
        letras = len(l)
        print(f"{l} possui {letras} letras")

palavras = ["casa", "paralelepípedo", "python"]

contar_letras(palavras)
'''
'''
#ex9
def converter_temperatura(temperaturas):
    for temp in temperaturas:
        fahrenheit = (temp * 1.8) + 32
        print(f"{temp} °C são {fahrenheit} °F")

temperaturas = [30, 100, 0]

converter_temperatura(temperaturas)
'''
'''
#ex10
def classificar_numeros(numeros):
    for n in numeros:
        if 0 <= n <= 5:
            print(f"{n} é Pequeno")
        elif 6 <= n <= 10:
            print(f"{n} é Médio")
        else:
            print(f"{n} é Grande")

numeros = [3, 9, 12]

classificar_numeros(numeros)
'''
'''
#ex11
def palindromos(palavras):
    for p in palavras:
        limpa = p.lower().replace(" ", "").strip()
        if limpa == limpa[::-1]:
            print(f"{p} é um palíndromo.")
        else:
            print(f"{p} não é um palíndromo.")

palavras = ['Ana Ana', '1DSTB-SENAI', 'Subi no Onibus']

palindromos(palavras)
'''
'''
#ex12
def fatorial(numeros):
    for num in numeros:
        if num > 0:
            resultado = 1
            for n in range(1, num + 1):
                resultado *= n
            print(f"{num}! = {resultado}")
        else:
            print("O número não poder negativo")


numeros = [3, 7, 9, 25, 26]

fatorial(numeros)
'''