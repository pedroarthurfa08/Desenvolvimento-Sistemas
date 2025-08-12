function getByid(id) {
    return document.getElementById(id);
}

const levels = [
    { id: 1, name: 'Fase1' },
    { id: 2, name: 'Fase2' },
    { id: 3, name: 'Fase3' },
    { id: 4, name: 'Fase4' },
    { id: 5, name: 'Fase5' },
    { id: 6, name: 'Fase6' },
    { id: 7, name: 'Fase7' },
    { id: 8, name: 'Fase8' },
    { id: 9, name: 'Fase9' },
    { id: 10, name: 'Fase10' },
    { id: 11, name: 'Fase11' },
    { id: 12, name: 'Fase12' }
];

let selectedCharacter = null;

const Cards = document.querySelectorAll('.level');

Cards.forEach(card => {
    card.addEventListener('click', () => {
        Cards.forEach(c => c.classList.remove('selected'));

        card.classList.add('selected');

        selectedCharacter = levels.find(level => 
            level.id === parseInt(card.dataset.id)
        );

        console.log(`Fase selecionada: ${selectedCharacter ? selectedCharacter.name : 'Nenhuma'}`);
    });
});

const b1 = getByid('b1');
b1.addEventListener('click', seleciona);

function seleciona() {
    if (selectedCharacter) {
        console.log(`Redirecionando para pergunta ${selectedCharacter.id}...`);

        setTimeout(() => {
            window.location.href = `../4pg_perguntas/Perguntas/pergunta${selectedCharacter.id}.html`;
        }, 1);
    } else {
        alert("Nenhuma fase foi selecionada!");
    }
}

// Elementos do DOM
const levelCards = document.querySelectorAll('.level');
const selectButton = document.getElementById('b1');
const toggleAudio = document.getElementById('toggleAudio');
const toggleContraste = document.getElementById('toggleContraste');
const aumentarFonte = document.getElementById('aumentarFonte');
const modal = document.getElementById('ajudaModal');
const fecharAjuda = document.getElementById('fecharAjuda');

// Estado da aplicação
let selectedLevel = null;
let audioHabilitado = false;
let altoContraste = false;
let fonteGrande = false;

// Configurações de áudio
const audioFeedback = new Audio('../1pg_principal/audio/feedback.mp3');
audioFeedback.volume = 0.5;

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    carregarPreferencias();
    inicializarAcessibilidade();
    adicionarEventListeners();
    verificarNomeUsuario();
});

// Funções principais
function verificarNomeUsuario() {
    const preferencias = JSON.parse(localStorage.getItem('interautPrefs')) || {};
    if (!preferencias.nomeUsuario) {
        // Se o nome não estiver salvo, redireciona para a página principal
        window.location.href = '../1pg_principal/index.html';
    }
}

function selecionarFase(card) {
    // Remove seleção anterior
    if (selectedLevel) {
        selectedLevel.classList.remove('selected');
        selectedLevel.setAttribute('aria-selected', 'false');
    }

    // Seleciona novo card
    selectedLevel = card;
    card.classList.add('selected');
    card.setAttribute('aria-selected', 'true');
    
    if (audioHabilitado) {
        audioFeedback.play();
    }
}

function iniciarFase() {
    if (!selectedLevel) {
        alert("Por favor, selecione uma fase para continuar!"); // Melhorar com modal
        return;
    }

    const faseId = selectedLevel.dataset.id;
    // Salvar o ID da fase selecionada para usar na próxima página
    localStorage.setItem('faseSelecionada', faseId);

    // Redireciona para a página de perguntas da fase selecionada
    setTimeout(() => {
        window.location.href = `../4pg_perguntas/Perguntas/pergunta${faseId}.html`;
    }, 200);
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
        } else if (e.key === 'Escape') {
            window.location.href = '../2pg_personagens/index.html';
        }
    });

    // Navegação por teclado entre cards
    levelCards.forEach((card, index) => {
        card.addEventListener('keydown', (e) => {
            switch(e.key) {
                case 'Enter':
                case ' ':
                    selecionarFase(card);
                    break;
                case 'ArrowRight':
                case 'ArrowDown':
                    e.preventDefault();
                    const nextCard = levelCards[index + 1] || levelCards[0];
                    nextCard.focus();
                    break;
                case 'ArrowLeft':
                case 'ArrowUp':
                    e.preventDefault();
                    const prevCard = levelCards[index - 1] || levelCards[levelCards.length - 1];
                    prevCard.focus();
                    break;
            }
        });
    });
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
    if (modal.style.display === 'block') {
        modal.focus();
    } else {
        selectButton.focus(); // Retorna o foco ao botão de seleção quando o modal é fechado
    }
}

// Gerenciamento de estado
function salvarPreferencias() {
    const preferencias = JSON.parse(localStorage.getItem('interautPrefs')) || {};
    preferencias.audioHabilitado = audioHabilitado;
    preferencias.altoContraste = altoContraste;
    preferencias.fonteGrande = fonteGrande;
    localStorage.setItem('interautPrefs', JSON.stringify(preferencias));
}

function carregarPreferencias() {
    try {
        const preferencias = JSON.parse(localStorage.getItem('interautPrefs')) || {};
        audioHabilitado = preferencias.audioHabilitado || false;
        altoContraste = preferencias.altoContraste || false;
        fonteGrande = preferencias.fonteGrande || false;

        // Aplicar preferências
        if (altoContraste) toggleAltoContraste();
        if (fonteGrande) toggleFonteGrande();
        if (audioHabilitado) toggleAudioFeedback();
    } catch (error) {
        console.error('Erro ao carregar preferências:', error);
    }
}

// Event Listeners
function adicionarEventListeners() {
    levelCards.forEach(card => {
        card.addEventListener('click', () => selecionarFase(card));
    });

    selectButton.addEventListener('click', iniciarFase);
    toggleAudio.addEventListener('click', toggleAudioFeedback);
    toggleContraste.addEventListener('click', toggleAltoContraste);
    aumentarFonte.addEventListener('click', toggleFonteGrande);
    fecharAjuda.addEventListener('click', toggleAjuda);

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