let visivel = false;
const meuElemento = document.getElementByIdleDeadline('meuElemento');
function exibirOcultar(){
    if (visivel) {
        meuElemento.style.visibility = 'hidden';
        visivel = false
    } else {
        meuElemento.style.visibility = 'visible';
        visivel = true;
    }
}