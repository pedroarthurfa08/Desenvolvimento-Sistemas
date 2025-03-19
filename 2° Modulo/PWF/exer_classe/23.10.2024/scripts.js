//alert('olá mundo de dentro de um arquivo externo');

var botao1 = document.getElementById('botao1');
botao1.addEventListener('click', cliqueDoBotao1);

function cliqueDoBotao1() {
    alert('Você clicou no botão');
}


var botao2 = document.getElementById('botao2');
botao2.addEventListener('click', cliqueDoBotao2);

function cliqueDoBotao2() {
    alert('Você clicou no botão 2');
}

var botao3 = document.getElementById('botao3');
botao3.addEventListener('click', cliqueDoBotao3);

function cliqueDoBotao3() {
    var resultado3 = document.getElementById('resultado3');
    resultado3.innerHTML = 'Você clicou no botão 3';
}    


var botao4 = document.getElementById('botao4');
botao4.addEventListener('mouseover', mouseSobreBotao4);
botao4.addEventListener('mouseout', mouseSaiuBotao4);

function mouseSobreBotao4() {
    alert('Você passou o mouse sobre o botão 4');
}

function mouseSaiuBotao4() {
    alert('Você tirou o mouse do botão 4');
}

var botao5 = document.getElementById('botao5');
botao5.addEventListener('click', clickDoBotao5);

function clickDoBotao5() {
    //var resultado5 = document.getElementById('resultado5');
    var a = 15;
    resultado5.innerHTML = 'Você clicou no botão 5 e a variável a é igual a ' + a;
}

var botao6 = document.getElementById('botao6');
botao6.addEventListener('click', clickDoBotao6);

function clickDoBotao6() {
    var resultado6 = document.getElementById('resultado6');
    var caixaTexto6 = document.getElementById('caixaTexto6');

    resultado6.innerHTML = 'Você digitou: ' + caixaTexto6.value;
 }

    var botao7 = document.getElementById('botao7');
    botao7.addEventListener('click', clickDoBotao7);

    function clickDoBotao7() {
        var resultado7 = document.getElementById('resultado7');
        var numero = Math.random() * 100;
        numero = parseInt(numero);
        resultado7.innerHTML = numero;
    }

    var botao8 = document.getElementById('botao8');
    botao8.addEventListener('click', clickDoBotao8);

    function clickDoBotao8() {
        var resultado8 = document.getElementById('resultado8');
        var caixaTexto8 = document.getElementById('caixaTexto8');
        var texto = caixaTexto8.value;
        var textoMaiusculo = texto.toUpperCase();
        resultado8.innerHTML = textoMaiusculo;
    }

    var botaoSomar = document.getElementById('botaoSomar');
    botaoSomar.addEventListener('click', clickDoBotaoSomar);

    function clickDoBotaoSomar() {
        var resultadoSoma = document.getElementById('resultadoSoma');
        var valor1 = parseInt(document.getElementById('caixaTextoValor1').value);
        var valor2 = parseInt(document.getElementById('caixaTextoValor2').value);

        var soma = valor1 + valor2;

        resultadoSoma.innerHTML = soma;
    }