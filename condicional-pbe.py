'''
#ex1
numero = int(input("Digite um número:"))
if numero%2 == 0:
    print("o número é par")
else:
    print("O número é ímpar")
'''
'''
#ex2
numero = int(input("Digite um número:"))
if numero>10:
    print("O número é maior que 10")
elif numero<10:
    print("O número é menor que 10")
else:
    print("O número é igual a 10")
'''
'''
#ex3
idade = int(input("Digite sua idade:"))
if idade >=18:
    print("Maior de idade")
else:
    print("Menor de idade")
'''
'''
#ex4
idade = int(input("Informe sua idade:"))

if  18 <= idade < 70:
    print("Voto obrigatório")
elif 16 <= idade <18 or idade >70:
    print("Voto opcional")
else:
    print("Não eleitor")
'''
'''
#ex5
numero = float(input("Digite um número:"))
if numero<0:
    print("O número é negativo")
elif numero>0:
    print("O número é positivo")
else:
    print("O número é igual a zero")
'''
'''
#ex6
nota = float(input("Digite sua nota:"))

if 9 <= nota <= 10:
    print("Sua nota é A")
elif 7 <= nota < 9:
    print("Sua nota é B")
elif 5 <= nota < 7:
    print("Sua nota é C")
elif 3 <= nota < 5:
    print("Sua nota é D")
elif 0 <= nota < 3:
    print("Sua nota é E")
else:
    print("Nota inválida.")
'''
'''
#ex7
idade = int(input("Informe sua idade:"))
if 13<= idade <=59:
    print("Não possui desconto")
else:
    print("Possui desconto")
'''
'''
#ex8
x = float(input("primeiro lado:"))
y = float(input("segundo lado:"))
z = float(input("terceiro lado:"))

if x + y > z and y + z > x and z + x > y:
    if x == y == z:
        print("O triângulo é equilátero")
    elif x != y != z:
        print("O triângulo é escaleno")
    else:
        print("O triângulo é isósceles")
else:
    print("Não forma um triângulo")
'''
'''
#ex9
valor = float(input("Informe o valor total da compra:"))
if valor <100:
    desconto = valor*0.05
    print(f"O desconto foi de {desconto} reais")
    print(f"O valor total com desconto é:{valor-desconto}")
elif 100<= valor <500:
    desconto = valor*0.1
    print(f"O desconto foi de {desconto} reais")
    print(f"O valor total com desconto é:{valor-desconto}")
else:
    desconto = valor*0.15
    print(f"O desconto foi de {desconto} reais")
    print(f"O valor total com desconto é:{valor-desconto}")
'''
'''
#ex10
ano = int(input("Digite o ano:"))
if ano%4 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
'''
'''
#ex11
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura(m):"))
imc = peso/(altura**2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")
'''
'''
#ex12
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))
if num1 < num2 < num3:
    print("Os números estão em ordem crescente")
elif num1 > num2 > num3:
    print("Os números estão em ordem drecrescente")
elif num1 == num2 == num3:
    print("Os números são iguais")
else:
    print("Os números estão em ordem aleatória")
'''
'''
#ex13
temp = float(input("Informe a temperatura:"))
if temp < 10:
    print("Frio")
elif 10 <= temp <=25:
    print("Aconchegante")
elif 25 < temp <=40:
    print("Quente")
else:
    print("Muito quente")
'''
'''
#ex14
data = input("Digite uma data no formato dd/mm/aaaa: ")

if "/" in data and len(data) == 10:
    partes = data.split("/")

    if len(partes) == 3 and all(p.isdigit() for p in partes):
        dia, mes, ano = partes
        data_formatada = f"{ano}-{mes}-{dia}"
        print(f"Data convertida: {data_formatada}")
    else:
        print("Formato inválido! Certifique-se de usar números no formato dd/mm/aaaa.")
else:
    print("Formato inválido! Certifique-se de usar dd/mm/aaaa.")
'''
'''
#ex15
import re

senha = input("Digite sua senha: ")

if len(senha) < 8:
    print("A senha deve ter pelo menos 8 caracteres.")
elif not any(c.isupper() for c in senha):
    print("A senha deve conter pelo menos uma letra maiúscula.")
elif not any(c.islower() for c in senha):
    print("A senha deve conter pelo menos uma letra minúscula.")
elif not any(c.isdigit() for c in senha):
    print("A senha deve conter pelo menos um número.")
elif not re.search(r"[@#$%&]", senha):
    print("A senha deve conter pelo menos um caractere especial (@, #, $, %, &).")
else:
    print("Senha válida!")
'''
'''
#ex16
num = float(input("Digite um número:"))

if num <0:
    print("Não é possível calcular a raiz quadrada de um número negativo.")
elif num >100:
    print("Número muito grande, reduza para um valor abaixo de 100.")
else:
    raiz = num ** 0.5
    print(f"Raiz quadrada:{raiz:.2f}")
'''
'''
#ex17
data = input("Digite a data no formato dd/mm/aaaa: ")
partes = data.split('/')

if len(partes) != 3:
    print("Data inválida")
else:
    dia, mes, ano = partes

    if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
        print("Data inválida")
    else:
        dia, mes, ano = int(dia), int(mes), int(ano)

        if mes < 1 or mes > 12:
            print("Data inválida")
        elif ano < 1:
            print("Data inválida")
        else:
            if mes in (1, 3, 5, 7, 8, 10, 12):
                max_dia = 31
            elif mes in (4, 6, 9, 11):
                max_dia = 30
            else:  # Fevereiro
                if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                    max_dia = 29  # Ano bissexto
                else:
                    max_dia = 28  # Ano comum

            if dia < 1 or dia > max_dia:
                print("Data inválida")
            else:
                print(f"{ano:04d}-{mes:02d}-{dia:02d}")
'''
'''
#ex18
import re


def evaluate_expression():
    variables = {}
    expression = input("Digite uma expressão matemática (use letras para variáveis, ex: a + b * c): ")

    variable_names = set(re.findall(r'[a-zA-Z]+', expression))

    for var in variable_names:
        value = input(f"Digite o valor de {var}: ")
        if not re.fullmatch(r'\d+(\.\d+)?', value):
            print("Valor inválido. Use apenas números.")
            return
        variables[var] = value

    for var, value in variables.items():
        expression = expression.replace(var, value)

    if not re.fullmatch(r'[0-9+\-*/(). ]+', expression):
        print("Expressão contém caracteres inválidos.")
        return

    result = eval(expression, {"__builtins__": None}, {})
    print("Resultado:", result)


evaluate_expression()
'''
'''
#ex19
import re

cpf = input("Digite um CPF: ")
cpf = re.sub(r'\D', '', cpf)  # Remove caracteres não numéricos

if len(cpf) != 11:
    print("CPF Inválido")
elif cpf == cpf[0] * 11:  # Verifica se todos os dígitos são iguais (caso inválido)
    print("CPF Inválido")
else:
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto1 = soma1 % 11
    if resto1 < 2:
        digito1 = '0'
    else:
        digito1 = str(11 - resto1)

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto2 = soma2 % 11
    if resto2 < 2:
        digito2 = '0'
    else:
        digito2 = str(11 - resto2)

    if cpf[-2:] == digito1 + digito2:
        print("CPF Válido")
    else:
        print("CPF Inválido")
'''