
async function searchPokemon() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const resultDiv = document.getElementById('result');
    
    if (!searchInput) {
        resultDiv.innerHTML = '<p class="error">Por favor, digite um nome ou número de Pokémon.</p>';
        return;
    }

    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${searchInput}`);
        if (!response.ok) throw new Error('Pokémon não encontrado!');
        
        const data = await response.json();
        
        const html = `
            <div class="pokemon-card">
                <img src="${data.sprites.other['official-artwork'].front_default}" 
                     alt="${data.name}">
                <h2>${data.name.charAt(0).toUpperCase() + data.name.slice(1)}</h2>
                <p>Número: #${String(data.id).padStart(3, '0')}</p>
                <p>Altura: ${data.height/10} m</p>
                <p>Peso: ${data.weight/10} kg</p>
                <div class="types">
                    ${data.types.map(type => `
                        <span class="type">${type.type.name}</span>
                    `).join('')}
                </div>
            </div>
        `;
        
        resultDiv.innerHTML = html;
    } catch (error) {
        resultDiv.innerHTML = `<p class="error">${error.message}</p>`;
    }
}

document.getElementById('searchInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchPokemon();
    }
});
