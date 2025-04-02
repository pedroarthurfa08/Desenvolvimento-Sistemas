def encontrar_maior_menor():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")

encontrar_maior_menor()