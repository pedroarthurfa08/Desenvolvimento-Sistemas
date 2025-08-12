// Elementos do DOM
const answerButtons = document.querySelectorAll('.resposta');
const resultMessage = document.getElementById('mensagem');
const popup = document.getElementById('popup');
const overlay = document.getElementById('overlay');
const nextButton = document.getElementById('proximoBotao');
const tryAgainButton = document.getElementById('tentarNovamenteBotao');
const scoreDisplay = document.getElementById('pontuacao');
const popupScoreDisplay = document.getElementById('score');
const audioButton = document.getElementById('baud');
const audioPlayer = document.getElementById('audio');
const toggleAudio = document.getElementById('toggleAudio');
const toggleContraste = document.getElementById('toggleContraste');
const aumentarFonte = document.getElementById('aumentarFonte');
const modal = document.getElementById('ajudaModal');
const fecharAjuda = document.getElementById('fecharAjuda');
const homeButton = document.getElementById('homeButtom');

// Estado da aplicação
let currentScore = 0;
let audioEnabled = false;
let highContrast = false;
let largeFont = false;
let currentQuestionId = 1; // Deve ser dinamicamente carregado da URL

// Configurações de áudio
const feedbackAudio = new Audio('../../1pg_principal/audio/feedback.mp3');
feedbackAudio.volume = 0.5;

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    loadPreferences();
    initializeAccessibility();
    addEventListeners();
    updateScoreDisplay();
    loadQuestionIdFromUrl();
});

// Funções principais
function loadQuestionIdFromUrl() {
    const urlParts = window.location.href.split('/');
    const fileName = urlParts[urlParts.length - 1];
    const match = fileName.match(/pergunta(\d+).html/);
    if (match && match[1]) {
        currentQuestionId = parseInt(match[1]);
    }
}

function checkAnswer(selectedButton) {
    answerButtons.forEach(button => {
        button.disabled = true;
        button.style.opacity = '0.5';
    });

    const isCorrect = selectedButton.dataset.correta === 'true';

    if (isCorrect) {
        currentScore += 3;
        localStorage.setItem('pontuacao', currentScore);
        updateScoreDisplay();

        resultMessage.textContent = 'Resposta correta!';
        resultMessage.style.color = 'var(--success-color)';
        nextButton.style.display = 'inline-block';
        tryAgainButton.style.display = 'none';
    } else {
        resultMessage.textContent = 'Resposta incorreta!';
        resultMessage.style.color = 'var(--error-color)';
        nextButton.style.display = 'none';
        tryAgainButton.style.display = 'inline-block';
    }

    popupScoreDisplay.textContent = currentScore;
    popup.style.display = 'block';
    overlay.style.display = 'block';

    if (audioEnabled) {
        feedbackAudio.play();
    }
}

function nextPhase() {
    if (currentQuestionId < 12) {
        currentQuestionId++;
        window.location.href = `pergunta${currentQuestionId}.html`;
    } else {
        alert("Você completou todas as fases!"); // Melhorar com modal
        setTimeout(() => {
            window.location.href = '../../5pg_final/index.html';
        }, 500);
    }
    closePopup();
}

function tryAgain() {
    location.reload();
}

function closePopup() {
    popup.style.display = 'none';
    overlay.style.display = 'none';
    answerButtons.forEach(button => {
        button.disabled = false;
        button.style.opacity = '1';
    });
}

function playAudioDescription() {
    if (audioPlayer) {
        audioPlayer.play();
    }
}

// Funções de acessibilidade
function initializeAccessibility() {
    // Atalhos de teclado
    document.addEventListener('keydown', (e) => {
        if (e.altKey) {
            switch(e.key) {
                case 'a':
                    toggleAudioFeedback();
                    break;
                case 'c':
                    toggleHighContrast();
                    break;
                case 'f':
                    toggleLargeFont();
                    break;
                case 'h':
                    toggleHelp();
                    break;
            }
        } else if (e.key === 'Escape') {
            window.location.href = '../../3pg_fases/index.html';
        }
    });

    // Navegação por teclado para botões de resposta
    answerButtons.forEach((button, index) => {
        button.addEventListener('keydown', (e) => {
            switch(e.key) {
                case 'Enter':
                case ' ':
                    checkAnswer(button);
                    break;
                case 'ArrowRight':
                    e.preventDefault();
                    const nextButtonInRow = Array.from(answerButtons).find((btn, i) => i > index && btn.parentElement === button.parentElement);
                    if (nextButtonInRow) {
                        nextButtonInRow.focus();
                    } else {
                        // Move to first button in next row or first overall if last row
                        const nextRowButtons = Array.from(answerButtons).filter((btn, i) => i > index && btn.parentElement.compareDocumentPosition(button.parentElement) & Node.DOCUMENT_POSITION_FOLLOWING);
                        if (nextRowButtons.length > 0) {
                            nextRowButtons[0].focus();
                        } else {
                            answerButtons[0].focus();
                        }
                    }
                    break;
                case 'ArrowLeft':
                    e.preventDefault();
                    const prevButtonInRow = Array.from(answerButtons).findLast((btn, i) => i < index && btn.parentElement === button.parentElement);
                    if (prevButtonInRow) {
                        prevButtonInRow.focus();
                    } else {
                        // Move to last button in previous row or last overall if first row
                        const prevRowButtons = Array.from(answerButtons).filter((btn, i) => i < index && btn.parentElement.compareDocumentPosition(button.parentElement) & Node.DOCUMENT_POSITION_PRECEDING);
                        if (prevRowButtons.length > 0) {
                            prevRowButtons[prevRowButtons.length - 1].focus();
                        } else {
                            answerButtons[answerButtons.length - 1].focus();
                        }
                    }
                    break;
                case 'ArrowDown':
                    e.preventDefault();
                    // Find next button in the same column
                    const currentColumn = Array.from(button.parentElement.children).indexOf(button);
                    const nextRow = button.parentElement.nextElementSibling;
                    if (nextRow && nextRow.children[currentColumn]) {
                        nextRow.children[currentColumn].focus();
                    } else if (index + 2 < answerButtons.length) { // Try to jump two buttons if in 2-column layout
                        answerButtons[index + 2].focus();
                    }
                    break;
                case 'ArrowUp':
                    e.preventDefault();
                    // Find previous button in the same column
                    const prevRow = button.parentElement.previousElementSibling;
                    if (prevRow && prevRow.children[currentColumn]) {
                        prevRow.children[currentColumn].focus();
                    } else if (index - 2 >= 0) { // Try to jump two buttons if in 2-column layout
                        answerButtons[index - 2].focus();
                    }
                    break;
            }
        });
    });
}

function toggleAudioFeedback() {
    audioEnabled = !audioEnabled;
    toggleAudio.setAttribute('aria-pressed', audioEnabled);
    toggleAudio.innerHTML = `<i class="fas fa-volume-${audioEnabled ? 'up' : 'mute'}" aria-hidden="true"></i>`;
    savePreferences();
}

function toggleHighContrast() {
    highContrast = !highContrast;
    document.body.classList.toggle('high-contrast');
    toggleContraste.setAttribute('aria-pressed', highContrast);
    savePreferences();
}

function toggleLargeFont() {
    largeFont = !largeFont;
    document.body.classList.toggle('large-text');
    aumentarFonte.setAttribute('aria-pressed', largeFont);
    savePreferences();
}

function toggleHelp() {
    const isVisible = modal.style.display === 'block';
    modal.style.display = isVisible ? 'none' : 'block';
    if (modal.style.display === 'block') {
        modal.focus();
    } else {
        // Retornar foco ao último elemento interativo antes de abrir o modal
        const lastFocusedElement = document.querySelector('*:focus');
        if (lastFocusedElement) {
            lastFocusedElement.focus();
        } else {
            answerButtons[0].focus(); // Fallback
        }
    }
}

// Gerenciamento de estado e UI
function updateScoreDisplay() {
    currentScore = parseInt(localStorage.getItem('pontuacao')) || 0;
    scoreDisplay.textContent = `${currentScore}`;
}

function savePreferences() {
    const preferences = JSON.parse(localStorage.getItem('interautPrefs')) || {};
    preferences.audioHabilitado = audioEnabled;
    preferences.altoContraste = highContrast;
    preferences.fonteGrande = largeFont;
    localStorage.setItem('interautPrefs', JSON.stringify(preferences));
}

function loadPreferences() {
    try {
        const preferences = JSON.parse(localStorage.getItem('interautPrefs')) || {};
        audioEnabled = preferences.audioHabilitado || false;
        highContrast = preferences.altoContraste || false;
        largeFont = preferences.fonteGrande || false;

        // Aplicar preferências
        if (highContrast) toggleHighContrast();
        if (largeFont) toggleLargeFont();
        if (audioEnabled) toggleAudioFeedback();
    } catch (error) {
        console.error('Erro ao carregar preferências:', error);
    }
}

// Event Listeners
function addEventListeners() {
    answerButtons.forEach(button => {
        button.addEventListener('click', () => checkAnswer(button));
    });

    nextButton.addEventListener('click', nextPhase);
    tryAgainButton.addEventListener('click', tryAgain);
    audioButton.addEventListener('click', playAudioDescription);
    toggleAudio.addEventListener('click', toggleAudioFeedback);
    toggleContraste.addEventListener('click', toggleHighContrast);
    aumentarFonte.addEventListener('click', toggleLargeFont);
    fecharAjuda.addEventListener('click', toggleHelp);

    if (homeButton) {
        homeButton.addEventListener('click', () => {
            localStorage.removeItem('pontuacao'); // Reinicia apenas a pontuação
        });
    }

    // Fechar modal de ajuda ao clicar fora
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            toggleHelp();
        }
    });
}

// Animações (se aplicável, com base nos estilos CSS)
document.querySelectorAll('.fade-in').forEach(element => {
    element.addEventListener('animationend', () => {
        element.classList.remove('fade-in');
    });
});