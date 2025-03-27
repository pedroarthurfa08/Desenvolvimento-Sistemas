class Aluno {
    constructor(nome, matricula){
        this.nome = nome;
        this.matricula = matricula;
        this.notaBimestral1 = 0;
        this.notaBimestral2 = 0;
    }

    Media(){
        return ((this.notaBimestral1 + this.notaBimestral2) / 2);
    }
}    


const al = new Aluno(11, 'Pedro')
console.log(al)

al.notaBimestral1 = 10
al.notaBimestral2 = 4

console.log(al.Media())