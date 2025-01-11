const passwordInput = document.getElementById('password');
        const errorMessage = document.getElementById('errorMessage');

        passwordInput.addEventListener('blur', () => {
            const password = passwordInput.value.trim(); // Remove espaços em branco
            if (password.length < 8) {
                errorMessage.style.display = 'block'; // Exibe a mensagem de erro
            } else {
                errorMessage.style.display = 'none'; // Oculta a mensagem de erro
            }
        });

        passwordInput.addEventListener('focus', () => {
            errorMessage.style.display = 'none'; // Oculta a mensagem ao focar novamente
        });