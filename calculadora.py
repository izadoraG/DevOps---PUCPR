import sys

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    else:
        return a / b

def main():
    if len(sys.argv) != 4:
        print("Uso: python3 calculadora.py <operação> <número1> <número2>")
        return

    operacao = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operacao == '1':
        print("Resultado:", adicao(num1, num2))
    elif operacao == '2':
        print("Resultado:", subtracao(num1, num2))
    elif operacao == '3':
        print("Resultado:", multiplicacao(num1, num2))
    elif operacao == '4':
        print("Resultado:", divisao(num1, num2))
    else:
        print("Escolha inválida!")

if __name__ == "__main__":
    main()
