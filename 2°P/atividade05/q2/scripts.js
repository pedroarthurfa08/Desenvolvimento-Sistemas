let tamanhoFonte = 16;
const texto = document.getElementById('texto');

function aumentarFonte() {
  tamanhoFonte += 2;
  texto.style.fontSize = tamanhoFonte + 'px';
}

function reduzirFonte() {
  tamanhoFonte -= 2;
  if (tamanhoFonte < 8) tamanhoFonte = 8; // Limite mínimo
  texto.style.fontSize = tamanhoFonte + 'px';
}