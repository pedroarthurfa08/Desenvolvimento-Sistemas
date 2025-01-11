const emotionSelect = document.getElementById('emotionSelect');
        const output = document.getElementById('output');

        emotionSelect.addEventListener('change', () => {
            const selectedEmotion = emotionSelect.value;
            output.textContent = selectedEmotion 
                ? `Você escolheu: ${selectedEmotion}` 
                : 'Por favor, selecione uma emoção.';
        });