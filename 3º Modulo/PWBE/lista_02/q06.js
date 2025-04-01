//Modifique a questão anterior para que o livro possa ter mais de um autor e adicione um método que imprima o nome completo de seus autores

class Autor {
    constructor(nome, sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
    }

    nomeCompleto() {
        return `${this.nome} ${this.sobrenome}`;
    }
}

class Livro {
    constructor(titulo, autores, pagina) {
        this.titulo = titulo;
        this.autores = autores; 
        this.pagina = pagina;
    }

    exibirAutores() {
        console.log("Autores:");
        this.autores.forEach(autor => {
            console.log(autor.nomeCompleto());
        });
    }

    exibirInfo() {
        console.log(`Título: ${this.titulo}`);
        this.exibirAutores(); 
        console.log(`Número de páginas: ${this.pagina}`);
    }
}

// Exemplo de uso
const autor1 = new Autor("J.K.", "Rowling");
const autor2 = new Autor("John", "Tolkien");

const livro1 = new Livro("Harry Potter e a Pedra Filosofal", [autor1, autor2], 223);

livro1.exibirInfo();
