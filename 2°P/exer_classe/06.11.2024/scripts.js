function getById(id) {
    return document.getElementById(id);
}

function clique(id, funcao) {
    getById(id).addEventListener('click', funcao); 
}

clique('botao1', () => {
    var botao1 = getById('botao1');
    getById('resultado1').innerHTML = "oi";
});


// Questão 1
/*
var botaoBoaTarde = document.getElementById('botaoBoaTarde');
botaoBoaTarde.addEventListener('click', boaTarde);

function boaTarde() {
    var resultadoSaudacao = document.getElementById('resultadoSaudacao');
    resultadoSaudacao.innerHTML = "boa tarde";
}

var botaoBoaNoite = document.getElementById('botaoBoaNoite');
botaoBoaNoite.addEventListener('click', boaNoite);

function boaNoite() {
    var resultadoSaudacao = document.getElementById('resultadoSaudacao');
    resultadoSaudacao.innerHTML = "boa noite";
} */

// Questão 01 resumida    
/*
clique('botaoBoaTarde', () => {
    getById('resultadoSaudacao').innerHTML = "boa tarde";
});

clique('botaoBoaNoite', () => {
    getById('resultadoSaudacao').innerHTML = "boa noite";
});
*/

// Questão 02
/*
var botaoBoaTarde = document.getElementById('botaoBoaTarde');
botaoBoaTarde.addEventListener('click', boaTarde);

function boaTarde() {
    var resultadoSaudacao = document.getElementById('resultadoSaudacao');
    var nome = document.getElementById('nome').value;
    resultadoSaudacao.innerHTML = "boa tarde, " + nome;
}

var botaoBoaNoite = document.getElementById('botaoBoaNoite');
botaoBoaNoite.addEventListener('click', boaNoite);

function boaNoite() {
    var resultadoSaudacao = document.getElementById('resultadoSaudacao');
    var nome = document.getElementById('nome').value;
    resultadoSaudacao.innerHTML = "boa noite, " + nome;
}*/

// Questão 02 resumida

clique('botaoBoaTarde', () => {
    getById('resultadoSaudacao').innerHTML = 
                    'Boa tarde, ' + getById('nome').value;
});

clique('botaoBoaNoite', () => {
    getById('resultadoSaudacao').innerHTML = 
    'Boa noite, ' + getById('nome').value;
});

// Questão 03
/*
var botaoCalcular = document.getElementById('botaoCalcular');
botaoCalcular.addEventListener('click', calcular);

function calcular() {
    var numeroRandomico = parseInt(Math.random() * 10) + 1;
    
    var  texto3b = parseInt(document.getElementById('texto3b').value);
    var numeroAbsoluto = Math.abs(texto3b);

    var n1 = parseInt(document.getElementById('textoN1').value);
    var n2 = parseInt(document.getElementById('textoN2').value);
    var maximo = Math.max(n1, n2);

    var exponenciacao = Math.pow(n1, n2);

    var resultadoCalculos = document.getElementById('resultadoCalculos');
    resultadoCalculos.innerHTML =
        `<br>Resultados: <br>
         3)a) Número randômico: ${numeroRandomico} <br>
         3)b) Número absoluto: ${numeroAbsoluto} <br>
         3)c) Maior dos dois números: ${maximo} <br>
         4)d) Exponneciação: ${exponenciacao}
        `
}*/

clique('botaoCalcular', () => {
    var numeroRandomico = parseInt(Math.random() * 10) + 1;
    
    var  texto3b = parseInt(getById('texto3b').value);
    var numeroAbsoluto = Math.abs(texto3b);

    var n1 = parseInt(getById('textoN1').value);
    var n2 = parseInt(getById('textoN2').value);
    var maximo = Math.max(n1, n2);

    var exponenciacao = Math.pow(n1, n2);

    getById('resultadoCalculos').innerHTML =
        `<br>Resultados: <br>
         3a) Número randômico: ${numeroRandomico} <br>
         3b) Número absoluto: ${numeroAbsoluto} <br>
         3c) Maior dos dois números: ${maximo} <br>
         3d) Exponneciação: ${exponenciacao}
        `
});


// Questão 04
/*
var botao4 = document.getElementById('botao4');
botao4.addEventListener('click', questao4);

function questao4() {
    var texto4 = document.getElementById('texto4').value;

    var tamanho = texto4.length;
    var minusculo = texto4.toLowerCase();
    var semEspacos = texto4.trim();
    var tamanhoSemEspacos = semEspacos.trim().length;
    var substituido = texto4.replaceAll('a', '@')
                            .replaceAll('e', '3')
                            .replaceAll('i', '1')
                            .replaceAll('o', '0');

    var resultado4 = document.getElementById('resultado4');
    resultado4.innerHTML = 
        `
        <br>
        4a) Tamanho da string: ${tamanho} <br>
        4b) Minúsculo: ${minusculo} <br>
        4c) Substituído: ${substituido} <br>
        4d) Sem espaços: ${semEspacos} <br>
        Bônus - tamanho sem espaços: ${tamanhoSemEspacos}
        `  
} */

// Questão 04 resumida

clique('botao4', () => {
   
        var texto4 = getById('texto4').value;
    
        var tamanho = texto4.length;
        var minusculo = texto4.toLowerCase();
        var semEspacos = texto4.trim();
        var tamanhoSemEspacos = semEspacos.trim().length;
        var substituido = texto4.replaceAll('a', '@')
                                .replaceAll('e', '3')
                                .replaceAll('i', '1')
                                .replaceAll('o', '0');
    
        getById('resultado4').innerHTML = 
            `
            <br>
            4a) Tamanho da string: ${tamanho} <br>
            4b) Minúsculo: ${minusculo} <br>
            4c) Substituído: ${substituido} <br>
            4d) Sem espaços: ${semEspacos} <br>
            Bônus - tamanho sem espaços: ${tamanhoSemEspacos}
            `  
});