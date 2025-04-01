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
    constructor(titulo, autor, pagina) {
        this.titulo = titulo;
        this.autor = autor;
        this.pagina = pagina;  
    }

    exibirInfo() {
        console.log(`Título: ${this.titulo}`);
        console.log(`Autor: ${this.autor.nomeCompleto()}`);
        console.log(`Número de páginas: ${this.pagina}`);  
    }
}

const autor1 = new Autor("J.K.", "Rowling");  
const livro1 = new Livro("Harry Potter e a Pedra Filosofal", autor1, 223); 

livro1.exibirInfo();
