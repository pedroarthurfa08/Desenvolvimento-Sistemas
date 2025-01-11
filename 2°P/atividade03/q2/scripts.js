function calcular() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);

    if (!isNaN(num1) && !isNaN(num2) {
        const sum = num1 + nem2;
        const subtract = num2 - num1;
        const multiply = num1 * num2;
        const divide = num1 / num2;
    }

    const resultado = 
    Soma: ${num1} + ${num2} = ${sum}
    Subtração: ${num1} - ${num2} = ${subtract}
    Multiplicação: ${num1} * ${num2} = ${multiply}
    Divisão: ${num1} / ${num2} = ${divide};

    document.getElementById('resultado').innerHTML = resultado;
} else {
    alert("Digite número válidos!")
}
