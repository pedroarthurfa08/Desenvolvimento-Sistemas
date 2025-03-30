class Aluno {
    constructor(nome, matricula, notas) {
        this.nome = nome;
        this.matricula = matricula;
        this.notas = notas;
    }

    calcularMedia() {
        const somaNotas = this.notas.reduce((total, nota) => total + nota, 0);
        return somaNotas / this.notas.length;
    }

    verificarSituacao() {
        const media = this.calcularMedia();
        if (media >= 7) {
            return 'Aprovado';
        } else if (media >= 5) {
            return 'Recuperação';
        } else {
            return 'Reprovado';
        }
    }
}

const aluno1 = new Aluno('Roberto Carlos', 78945, [7, 3, 10, 5]);

console.log(`Aluno: ${aluno1.nome}`);
console.log(`Matrícula: ${aluno1.matricula}`);
console.log(`Média: ${aluno1.calcularMedia()}`);
console.log(`Situação: ${aluno1.verificarSituacao()}`);

const aluno2 = new Aluno('Galvão Bueno', 74402, [0, 36, 9, 10]);

console.log(`Aluno: ${aluno1.nome}`);
console.log(`Matrícula: ${aluno1.matricula}`);
console.log(`Média: ${aluno1.calcularMedia()}`);
console.log(`Situação: ${aluno1.verificarSituacao()}`);

const aluno3 = new Aluno('Frei Gilson', 95102, [10, 9, 4, 6]);

console.log(`Aluno: ${aluno1.nome}`);
console.log(`Matrícula: ${aluno1.matricula}`);
console.log(`Média: ${aluno1.calcularMedia()}`);
console.log(`Situação: ${aluno1.verificarSituacao()}`);
