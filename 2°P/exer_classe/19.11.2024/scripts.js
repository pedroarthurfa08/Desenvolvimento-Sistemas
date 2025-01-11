function getById(id) {
    return document.getElementById(id);
}

var verificar = getById('verificar');
verificar.addEventListener('click', () => {
    var numero = parseInt(getById('numero').value);
    var resultado = getById('resultado');

    if (numero > 10) {
        resultado.innerHTML = 'O número é maior que 10';
    } else {
        if (numero < 10) {
            resultado.innerHTML = 'O número é menor que 10';
        } else {
            resultado.innerHTML = 'O número é menor ou igual a 10';
        }
    }
});


var verificarDia = getById('verificarDia');
verificarDia.addEventListener('click', () => {
    var dia = getById('dia').value;
    var resultadoSwitch = getById('resultadoSwitch');

    switch (dia) {
        case '1':
            resultadoSwitch.innerHTML = 'Domingo';
            break;
        // demais "cases"
        case '7':
            resultadoSwitch.innerHTML = 'Sábado';
            break;
        default:
            resultadoSwitch.innerHTML = 'Dia inválido';
            break;
    }
});

var contar = getById('contar');
contar.addEventListener('click', () => {
    var resultadoFor = getById('resultadoFor');
    for (var i = 1; i <= 5 ; i++) {
        resultadoFor.innerHTML += i + ' ';
    }

    resultadoFor.innerHTML += "<br>Agora o inverso<br>";
    
    for (var i = 5; i >= 1 ; i--) {
        resultadoFor.innerHTML += i + ' ';
    }
});    

var mostrarArrayOf = getById('mostrarArrayOf');
mostrarArrayOf.addEventListener('click', () => {
    var resultadoForOf = getById('resultadoForOf');
    var frutas = ['uva', 'banana', 'pera', 'manga'];

    for (var fruta of frutas) {
        resultadoForOf.innerHTML += fruta + ' ';
    }

});

var mostrarArrayIn = getById('mostrarArrayIn');
mostrarArrayIn.addEventListener('click', () => {
    var resultadoForIn = getById('resultadoForIn');
    var cidades = ['the', 'sp', 'phb', 'slz', 'for'];

    for (var indice in cidades) {
        resultadoForIn.innerHTML +=  indice + ' ' + cidades[indice] + ' ';
    }
});

var contarWhile = getById('contarWhile');
contarWhile.addEventListener('click', () => {
    var resultadoWhile = getById('resultadoWhile');
    var limite = getById('limite').value;
    var contador = 1;
    
    resultadoWhile.innerHTML = '';

    while (contador <= limite) {
        resultadoWhile.innerHTML += contador + ' ';
        contador++;
    }
});

var contarDoWhile = getById('contarDoWhile');
contarDoWhile.addEventListener('click', () => {
    var resultadoDoWhile = getById('resultadoDoWhile');
    var limiteDoWhile = getById('limiteDoWhile').value;
    var contador = 1;

    resultadoDoWhile.innerHTML = '';

    do {
        resultadoDoWhile.innerHTML += contador + ' ';
        contador++;
    } while (contador <= limiteDoWhile);
});

var encontrarNumero = getById('encontrarNumero');
encontrarNumero.addEventListener('click', () => {
    var resultadoBreak = getById('resultadoBreak');
    var numeros = [1, 3, 4, 10, 2, 5, 15, 0, -1, 30];

    resultadoBreak.innerHTML = numeros + '<br>';

    for (var numero of numeros) {
        resultadoBreak.innerHTML += numero + ' ';
        if (numero > 10) {
            break;
        }
    }
});