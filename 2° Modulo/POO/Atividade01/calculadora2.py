class Calculadora:
    n1 = None
    n2 = None
    op = None

    def calcular(self, n1, n2, op):
        self.n1 = n1
        self.n2 = n2
        self.op = op

        if self.op == "+":
            return self.n1 + self.n2
        elif self.op == "-":
            return self.n1 - self.n2
        elif self.op == "*":
            return self.n1 * self.n2
        elif self.op == '/':
            if self.n2 != 0:
                return self.n1 / self.n2
            else:
                return("A divisão por zero não é permitida")
        else:
            return "Operação Inválida"

def main():
    mi_calc = Calculadora()
    while True:
        n1 = float(input("Digite um primeiro número: "))
        n2 = float(input("Digite um segundo número: "))

        op = input("Escolha a operação (+, -, *, /) ou 'q' para sair: ")
        
        if op == 'q':
            print("Encerrando a calculadora...")
            break

        resultado = mi_calc.calcular(n1, n2, op)
        print(f'{n1} {op} {n2} = {resultado}')
        
main()
