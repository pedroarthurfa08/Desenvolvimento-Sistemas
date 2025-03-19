function getById(id) {
    return document.getElementById(id);
}

let textoOrigem = getById('textoOrigem');
textoOrigem.addEventListener('keyup', () => { 
    let textoDestino = getById('textoDestino');
    textoDestino.value = textoOrigem.value;
});

let botaoMouse = getById('botaoMouse');
botaoMouse.addEventListener('mouseenter', () => {
    botaoMouse.innerHTML = 'Mouse sobre o botao';
});

botaoMouse.addEventListener('mouseleave', () => {
    botaoMouse.innerHTML = 'Mouse saiu do botao';
});



let botaoCarregarImagem = getById('botaoCarregarImagem');
let imagem1 = getById('imagem1');

botaoCarregarImagem.addEventListener('click', () => {
    let textoImagem = getById('textoImagem');
    imagem1.src = textoImagem.value;
});

imagem1.addEventListener('load', () => {
    let statusImagem = getById('statusImagem');
    statusImagem.innerHTML = 'Imagem carregada'
});

let cidades = getById('cidades');
cidades.addEventListener('change', () => {
    let cidadeSelecionada = getById('cidadeSelecionada');
    cidadeSelecionada.innerHTML = cidades.value;
});


let textoFoco = getById('textoFoco');
let statusFoco = getById('statusFoco');

textoFoco.addEventListener('focus', () => {
    statusFoco.innerHTML = 
        "caixa de texto ganhou o foco";
});

textoFoco.addEventListener('blur', () => {
    statusFoco.innerHTML = 
        "caixa de texto perdeu o foco";
});