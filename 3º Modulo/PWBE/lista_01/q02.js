function encontrarMaiorMenor() {
    const num1 = parseInt(prompt("Digite o primeiro número:"));
    const num2 = parseInt(prompt("Digite o segundo número:"));
    const num3 = parseInt(prompt("Digite o terceiro número:"));

    const maior = Math.max(num1, num2, num3);
    const menor = Math.min(num1, num2, num3);

    alert(`O maior número é: ${maior}`);
    alert(`O menor número é: ${menor}`);
}

encontrarMaiorMenor();