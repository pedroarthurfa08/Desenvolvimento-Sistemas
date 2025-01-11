function numeroAleatorio() {
    let numero = Math.floor(Math.random() * 10) + 1;
    document.getElementById('aleatorio').innerHTML = `O número número aleatório ${numero}.`;
}

function valorAbsoluto() {
    let numero = parseFloat(document.getElementById("numeroAbs").value);
    document.getElementById("absoluto").innerHTML = `O valor absoluto será ${Math.abs(numero)}`;
}

function maiorNumero() {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    document.getElementById("maior").innerHTML = `O maior número é ${Math.max(num1, num2)}`;
}

function arredondamento() {
    let numero = parseFloat(document.getElementById("arredondar").value);
    document.getElementById("arredondado").innerHTML = `Número arredondado: ${Math.round(numero)}`;
}

function potencia() {
    let base = parseFloat(document.getElementById("base").value);
    let expoente = parseFloat(document.getElementById("expoente").value);
    document.getElementById("potencia").innerHTML = `Potência: ${Math.pow(base, expoente)}`;
}

