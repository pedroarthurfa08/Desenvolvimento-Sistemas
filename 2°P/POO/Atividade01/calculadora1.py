def cal(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 != 0:
            return n1 / n2
        else:
            return "A divisão por zero não permitida"
    else:
        return "Operação Invalida"
def main():
    while True:
        try:
            n1 = float(input("Digite um primeiro número: "))
            n2 = float(input("Digite um segundo número: "))

            op = input("Digite a operação: ")

            if op =='q':
                print("Escolha a operação (+, -, *, /) ou 'q' para sair:")
                break
            
            resultado = cal(op, n1, n2)
            print(f"Resultado {resultado}")

        except ValueError:
            print("Insira valores númericos válidos.")
main()