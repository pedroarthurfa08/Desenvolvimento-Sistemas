function getByID(id) {
    return document.getElementById(id);
}

// Elementos do DOM
const botaoConsultar = getByID('botaoConsultar');
const botaoLimpar = getByID('botaoLimpar');
const botaoInverter = getByID('botaoInverter');
const moedaBaseInput = getByID('moedaBase');
const moedaConversaoInput = getByID('moedaConversao');
const resultado = getByID('resultado');

// Event Listeners
botaoConsultar.addEventListener('click', consultarPreco);
botaoLimpar.addEventListener('click', limparCampos);
botaoInverter.addEventListener('click', inverterMoedas);

// Função para validar campos
function validarCampos() {
    const moedaBase = moedaBaseInput.value.trim();
    const moedaConversao = moedaConversaoInput.value.trim();

    if (!moedaBase || !moedaConversao) {
        resultado.innerHTML = '<p class="error">Por favor, preencha ambos os campos de moeda.</p>';
        return false;
    }
    return true;
}

// Função para limpar campos
function limparCampos() {
    moedaBaseInput.value = '';
    moedaConversaoInput.value = '';
    resultado.innerHTML = '';
}

// Função para inverter moedas
function inverterMoedas() {
    const moedaBase = moedaBaseInput.value;
    const moedaConversao = moedaConversaoInput.value;
    
    moedaBaseInput.value = moedaConversao;
    moedaConversaoInput.value = moedaBase;
    
    if (moedaBase && moedaConversao) {
        consultarPreco();
    }
}

// Função principal de consulta
async function consultarPreco() {
    if (!validarCampos()) {
        return;
    }

    const moedaBase = moedaBaseInput.value.toUpperCase();
    const moedaConversao = moedaConversaoInput.value.toUpperCase();
    const url = `https://api.binance.com/api/v3/ticker/price?symbol=${moedaBase}${moedaConversao}`;

    try {
        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`Par de moedas inválido ou indisponível`);
        }

        const json = await response.json();
        
        resultado.innerHTML = `
            <p><strong>Par de Moedas:</strong> ${json.symbol}</p>
            <p><strong>Preço:</strong> ${parseFloat(json.price).toFixed(2)} ${moedaConversao}</p>
        `;
    } catch (error) {
        resultado.innerHTML = `<p class="error">Erro: ${error.message}</p>`;
    }
}