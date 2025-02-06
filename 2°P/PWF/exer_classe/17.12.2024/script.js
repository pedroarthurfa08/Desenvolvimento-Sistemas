function getById(id) {
    return document.getElementById(id);
}

let botaoAdicionar = getById('botaoAdicionar');

botaoAdicionar.addEventListener('click', adicionarParagrafo);

function adicionarParagrafo() {
    let textoParagrafo = getById('textoParagrafo').value;

    let paragrafo = document.createElement('p');
    paragrafo.innerHTML = textoParagrafo;

    let divParagrafos = getById('divParagrafos');
    divParagrafos.appendChild(paragrafo);
}


let botaoExcluir = getById('botaoExcluir');
let divElementos = getById('divElementos');

botaoExcluir.addEventListener('click', excluirElemento);

function excluirElemento() {
    let id = getById('textoId').value;
    let elemento = getById(id);
    divElementos.removeChild(elemento);
}

let botaoEndereco = getById('botaoEndereco')

botaoEndereco.addEventListener('click', alterarEndereco);
function alterarEndereco() {
    let textoLink = getById('textoLink').value;
    let link = getById('link');
    link.href = textoLink;
}

let botaoAdicionarOpcao = getById('botaoAdicionarOpcao');
botaoAdicionarOpcao.addEventListener('click', adicionarOpcao);

function adicionarOpcao() {
    let select = getById('select');
    let novaOpcao = getById('novaOpcao').value;

    let elemento = document.createElement('option');
    elemento.innerHTML = novaOpcao;

    select.appendChild(elemento);
}

let botaoRemoverOpcao = getById('botaoRemoverOpcao');
botaoRemoverOpcao.addEventListener('click', removerOpcao);

function removerOpcao() {
    let select = getById('select');
    let indiceSelecionado = select.selectedIndex;
    if (indiceSelecionado != -1) {
        select.remove(indiceSelecionado);
    }
}