const characters = [
    {
        id: 1,
        name: 'INTERAÇÃO',
    },    
];

const characterCards = document.querySelectorAll('.character-card');
const confirmationDiv = document.getElementById('confirmation');
const confirmButton = document.getElementById('confirm-button');
const confirmationMessage = document.getElementById('confirmation-message');
const selectedCharacterName = document.getElementById('selected-character-name');
const toggleAudio = document.getElementById('toggleAudio');
const toggleContraste = document.getElementById('toggleContraste');
const aumentarFonte = document.getElementById('aumentarFonte');
const modal = document.getElementById('ajudaModal');
const fecharAjuda = document.getElementById('fecharAjuda');

let selectedCard = null;
let audioHabilitado = false;
let altoContraste = false;
let fonteGrande = false;

const audioFeedback = new Audio('../1pg_principal/audio/feedback.mp3');
audioFeedback.volume = 0.5;

document.addEventListener('DOMContentLoaded', () => {
    carregarPreferencias();
    inicializarAcessibilidade();
    adicionarEventListeners();
    verificarNomeUsuario();
});

function verificarNomeUsuario() {
    const preferencias = JSON.parse(localStorage.getItem('interautPrefs')) || {};
    if (!preferencias.nomeUsuario) {
        window.location.href = '../1pg_principal/index.html';
    }
}

function selecionarCard(card) {
    if (selectedCard) {
        selectedCard.classList.remove('selected');
        selectedCard.setAttribute('aria-selected', 'false');
    }

    selectedCard = card;
    card.classList.add('selected');
    card.setAttribute('aria-selected', 'true');
    
    confirmationDiv.classList.remove('hidden');
    confirmButton.focus();

    if (audioHabilitado) {
        audioFeedback.play();
    }
}

function confirmarSelecao() {
    if (!selectedCard) return;

    const habilidade = selectedCard.querySelector('h2').textContent;
    selectedCharacterName.textContent = `Habilidade selecionada: ${habilidade}`;
    
    confirmationDiv.classList.add('hidden');
    confirmationMessage.classList.remove('hidden');
    
    localStorage.setItem('habilidadeSelecionada', habilidade);
    
    setTimeout(() => {
        window.location.href = '../3pg_fases/index.html';
    }, 2000);
}

function inicializarAcessibilidade() {
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
            window.location.href = '../1pg_principal/index.html';
        }
    });

    characterCards.forEach((card, index) => {
        card.setAttribute('tabindex', '0');
        card.setAttribute('role', 'button');
        card.setAttribute('aria-selected', 'false');

        card.addEventListener('keydown', (e) => {
            switch(e.key) {
                case 'Enter':
                case ' ':
                    selecionarCard(card);
                    break;
                case 'ArrowRight':
                case 'ArrowDown':
                    e.preventDefault();
                    const nextCard = characterCards[index + 1] || characterCards[0];
                    nextCard.focus();
                    break;
                case 'ArrowLeft':
                case 'ArrowUp':
                    e.preventDefault();
                    const prevCard = characterCards[index - 1] || characterCards[characterCards.length - 1];
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
}

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

        if (altoContraste) toggleAltoContraste();
        if (fonteGrande) toggleFonteGrande();
        if (audioHabilitado) toggleAudioFeedback();
    } catch (error) {
        console.error('Erro ao carregar preferências:', error);
    }
}

function adicionarEventListeners() {
    characterCards.forEach(card => {
        card.addEventListener('click', () => selecionarCard(card));
    });

    confirmButton.addEventListener('click', confirmarSelecao);
    toggleAudio.addEventListener('click', toggleAudioFeedback);
    toggleContraste.addEventListener('click', toggleAltoContraste);
    aumentarFonte.addEventListener('click', toggleFonteGrande);
    fecharAjuda.addEventListener('click', toggleAjuda);

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            toggleAjuda();
        }
    });
}

document.querySelectorAll('.fade-in').forEach(element => {
    element.addEventListener('animationend', () => {
        element.classList.remove('fade-in');
    });
});