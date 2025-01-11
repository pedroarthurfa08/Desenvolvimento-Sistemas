let visivel = false;
const meuElemento = document.getElementById('meuElemento');

function exibirOcultar() {
  if (visivel) {
    meuElemento.style.visibility = 'hidden';
    visivel = false;
  } else {
    meuElemento.style.visibility = 'visible';
    visivel = true;
  }
}