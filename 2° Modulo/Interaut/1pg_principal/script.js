// Elementos do DOM
const inputNome = document.getElementById('ct1');
const btnEnviar = document.getElementById('b2');
const btnIniciar = document.getElementById('b1');
const mensagem = document.getElementById('mensagem');
const titulo = document.getElementById('t1');
const toggleAudio = document.getElementById('toggleAudio');
const toggleContraste = document.getElementById('toggleContraste');
const aumentarFonte = document.getElementById('aumentarFonte');
const modal = document.getElementById('ajudaModal');
const fecharAjuda = document.getElementById('fecharAjuda');

// Estado da aplicação
let audioHabilitado = false;
let altoContraste = false;
let fonteGrande = false;
let nomeUsuario = '';

// Configurações de áudio
const audioFeedback = new Audio('audio/feedback.mp3');
audioFeedback.volume = 0.5;

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    carregarPreferencias();
    inicializarAcessibilidade();
    adicionarEventListeners();
});

// Funções principais
function perguntaNome() {
    const nome = inputNome.value.trim();
    if (nome === '') {
        mostrarMensagem('Por favor, digite seu nome.', 'error');
        inputNome.focus();
        return;
    }

    nomeUsuario = nome;
    salvarPreferencias();
    mostrarMensagem(`Olá, ${nome}! Bem-vindo(a) ao Interaut!`, 'success');
    habilitarBotaoIniciar();
}

function iniciarExperiencia() {
    if (!nomeUsuario) {
        mostrarMensagem('Por favor, digite seu nome primeiro.', 'error');
        inputNome.focus();
        return;
    }

    // Salvar estado antes de redirecionar
    salvarPreferencias();
    
    // Adicionar animações de saída
    document.querySelector('.divisao').classList.add('fade-out');
    
    // Redirecionar após a animação
    setTimeout(() => {
        window.location.href = '../2pg_personagens/index.html';
    }, 1000);
}

// Funções de acessibilidade
function inicializarAcessibilidade() {
    // Atalhos de teclado
    document.addEventListener('keydown', (e) => {
        if (e.altKey) {
            switch(e.key) {
                case 'a':
                    toggleAudioFeedback();
                    break;
                case 'c':
                    toggleAltoContraste();
                    break;
                case 'f':
                    toggleFonteGrande();
                    break;
                case 'h':
                    toggleAjuda();
                    break;
            }
        }
    });

    // Foco inicial
    inputNome.focus();
}

function toggleAudioFeedback() {
    audioHabilitado = !audioHabilitado;
    toggleAudio.setAttribute('aria-pressed', audioHabilitado);
    toggleAudio.innerHTML = `<i class="fas fa-volume-${audioHabilitado ? 'up' : 'mute'}" aria-hidden="true"></i>`;
    salvarPreferencias();
}

function toggleAltoContraste() {
    altoContraste = !altoContraste;
    document.body.classList.toggle('high-contrast');
    toggleContraste.setAttribute('aria-pressed', altoContraste);
    salvarPreferencias();
}

function toggleFonteGrande() {
    fonteGrande = !fonteGrande;
    document.body.classList.toggle('large-text');
    aumentarFonte.setAttribute('aria-pressed', fonteGrande);
    salvarPreferencias();
}

function toggleAjuda() {
    const estaVisivel = modal.style.display === 'block';
    modal.style.display = estaVisivel ? 'none' : 'block';
}

// Funções de UI
function mostrarMensagem(texto, tipo = 'info') {
    mensagem.textContent = texto;
    mensagem.className = `mensagem ${tipo}`;
    mensagem.parentElement.classList.add('fade-in');

    if (audioHabilitado) {
        audioFeedback.play();
    }
}

function habilitarBotaoIniciar() {
    btnIniciar.disabled = false;
    btnIniciar.classList.add('fade-in');
}

// Gerenciamento de estado
function salvarPreferencias() {
    const preferencias = {
        nomeUsuario,
        audioHabilitado,
        altoContraste,
        fonteGrande
    };
    localStorage.setItem('interautPrefs', JSON.stringify(preferencias));
}

function carregarPreferencias() {
    try {
        const preferencias = JSON.parse(localStorage.getItem('interautPrefs')) || {};
        nomeUsuario = preferencias.nomeUsuario || '';
        audioHabilitado = preferencias.audioHabilitado || false;
        altoContraste = preferencias.altoContraste || false;
        fonteGrande = preferencias.fonteGrande || false;

        // Aplicar preferências
        if (nomeUsuario) {
            inputNome.value = nomeUsuario;
            mostrarMensagem(`Bem-vindo(a) de volta, ${nomeUsuario}!`);
            habilitarBotaoIniciar();
        }
        if (altoContraste) toggleAltoContraste();
        if (fonteGrande) toggleFonteGrande();
        if (audioHabilitado) toggleAudioFeedback();
    } catch (error) {
        console.error('Erro ao carregar preferências:', error);
    }
}

// Event Listeners
function adicionarEventListeners() {
    btnEnviar.addEventListener('click', perguntaNome);
    btnIniciar.addEventListener('click', iniciarExperiencia);
    toggleAudio.addEventListener('click', toggleAudioFeedback);
    toggleContraste.addEventListener('click', toggleAltoContraste);
    aumentarFonte.addEventListener('click', toggleFonteGrande);
    fecharAjuda.addEventListener('click', toggleAjuda);

    inputNome.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            perguntaNome();
        }
    });

    // Fechar modal de ajuda ao clicar fora
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            toggleAjuda();
        }
    });
}

// Animações
document.querySelectorAll('.fade-in').forEach(element => {
    element.addEventListener('animationend', () => {
        element.classList.remove('fade-in');
    });
});