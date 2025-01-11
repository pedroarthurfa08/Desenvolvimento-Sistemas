function nomeCompleto() {
    let nome = document.getElementById("nome").value;
    let sobrenome = document.getElementById("sobrenome").value;
    document.getElementById("nome-completo").innerHTML = `Nome Completo: ${nome} ${sobrenome}`;
    }
    
    function somaEDiferenca() {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let soma = num1 + num2;
    let diferenca = num1 - num2;
    document.getElementById("resultado-soma").innerHTML = `Soma: ${soma}`;
    document.getElementById("resultado-diferenca").innerHTML = `Diferença: ${diferenca}`;
    }
    
    function limparCaixa() {
    document.getElementById("caixa").value = "";
    }
    
    function copiarTexto() {
    let textoOrigem = document.getElementById("caixa-origem").value;
    document.getElementById("caixa-destino").value = textoOrigem;
    }