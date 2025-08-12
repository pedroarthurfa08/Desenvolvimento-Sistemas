import '@testing-library/jest-dom';

// Mock do localStorage
const localStorageMock = {
    getItem: jest.fn(),
    setItem: jest.fn(),
    clear: jest.fn()
};
global.localStorage = localStorageMock;

// Mock do Audio
class AudioMock {
    constructor() {
        this.volume = 1;
        this.play = jest.fn();
        this.pause = jest.fn();
    }
}
global.Audio = AudioMock;

// Mock de funções do DOM
global.document.createRange = () => ({
    setStart: () => {},
    setEnd: () => {},
    commonAncestorContainer: {
        nodeName: 'BODY',
        ownerDocument: document,
    },
});

// Limpa mocks após cada teste
afterEach(() => {
    jest.clearAllMocks();
}); 