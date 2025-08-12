import { fireEvent, screen } from '@testing-library/dom';
import '@testing-library/jest-dom';

describe('Página Principal', () => {
    let container;

    beforeEach(() => {
        document.body.innerHTML = `
            <div class="divisao">
                <input id="ct1" type="text" placeholder="Digite seu nome">
                <button id="b2" onclick="perguntaNome()">Enviar</button>
                <button id="b1">Iniciar</button>
                <p id="mensagem"></p>
            </div>
        `;
        container = document.querySelector('.divisao');
    });

    test('deve exibir mensagem de erro quando nome estiver vazio', () => {
        const inputNome = screen.getByPlaceholderText('Digite seu nome');
        const btnEnviar = screen.getByText('Enviar');
        const mensagem = screen.getByText('');

        fireEvent.click(btnEnviar);

        expect(mensagem).toHaveTextContent('Por favor, digite seu nome.');
    });

    test('deve exibir mensagem de boas-vindas quando nome for válido', () => {
        const inputNome = screen.getByPlaceholderText('Digite seu nome');
        const btnEnviar = screen.getByText('Enviar');
        const mensagem = screen.getByText('');

        fireEvent.change(inputNome, { target: { value: 'João' } });
        fireEvent.click(btnEnviar);

        expect(mensagem).toHaveTextContent('Olá, João! Bem-vindo(a) ao Interaut!');
    });

    test('deve habilitar botão de iniciar após nome válido', () => {
        const inputNome = screen.getByPlaceholderText('Digite seu nome');
        const btnEnviar = screen.getByText('Enviar');
        const btnIniciar = screen.getByText('Iniciar');

        fireEvent.change(inputNome, { target: { value: 'João' } });
        fireEvent.click(btnEnviar);

        expect(btnIniciar).not.toBeDisabled();
    });

    test('deve salvar preferências no localStorage', () => {
        const inputNome = screen.getByPlaceholderText('Digite seu nome');
        const btnEnviar = screen.getByText('Enviar');

        fireEvent.change(inputNome, { target: { value: 'João' } });
        fireEvent.click(btnEnviar);

        expect(localStorage.setItem).toHaveBeenCalledWith(
            'interautPrefs',
            expect.any(String)
        );
    });
}); 