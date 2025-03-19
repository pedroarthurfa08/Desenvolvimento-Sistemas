const yearSelect = document.getElementById('yearSelect');
for (let year = 2024; year >= 1995; year--) {
    const option = document.createElement('option');
    option.value = year;
    option.textContent = year;
    yearSelect.appendChild(option);
}

async function loadMakes() {
    try {
        const response = await fetch('https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json');
        const data = await response.json();
        
        const makeSelect = document.getElementById('makeSelect');
        data.Results.forEach(make => {
            const option = document.createElement('option');
            option.value = make.Make_ID;
            option.textContent = make.Make_Name;
            makeSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Erro ao carregar marcas:', error);
    }
}

async function searchModels() {
    const make = document.getElementById('makeSelect').value;
    const year = document.getElementById('yearSelect').value;
    const resultsDiv = document.getElementById('results');

    if (!make || !year) {
        resultsDiv.innerHTML = '<div class="error">Por favor, selecione marca e ano.</div>';
        return;
    }

    resultsDiv.innerHTML = '<div class="loading">Carregando...</div>';

    try {
        const response = await fetch(
            `https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeIdYear/makeId/${make}/modelyear/${year}?format=json`
        );
        const data = await response.json();

        if (data.Results.length === 0) {
            resultsDiv.innerHTML = '<div class="error">Nenhum modelo encontrado para esta combinação de marca e ano.</div>';
            return;
        }

        resultsDiv.innerHTML = data.Results.map(model => `
            <div class="car-card">
                <div class="placeholder-img">
                    <span>🚗</span>
                </div>
                <h3>${model.Make_Name} ${model.Model_Name}</h3>
                <div class="car-info">
                    <p><strong>Ano:</strong> ${year}</p>
                    <p><strong>Modelo:</strong> ${model.Model_Name}</p>
                    <p><strong>Marca:</strong> ${model.Make_Name}</p>
                </div>
            </div>
        `).join('');

    } catch (error) {
        resultsDiv.innerHTML = '<div class="error">Erro ao buscar modelos. Tente novamente.</div>';
    }
}

loadMakes();