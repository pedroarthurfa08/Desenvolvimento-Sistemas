function inverterTexto() {
    
    var texto = document.getElementById('texto').value;
    var textoInvertido = texto.split('').reverse().join('');
    document.getElementById('resultado').innerHTML ='Texto Invertido: ' + textoInvertido;
}