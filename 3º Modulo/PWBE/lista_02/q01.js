//Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e métodos para calcular a área e o perímetro do círculo.//

class Circulo {
    constructor(raio) {
        this.raio = raio;
    }

    calcularArea(){
        return Math.PI * Math.pow(this.raio, 2);
    }

    calcularPerimetro(){
        return 2 * Math.PI * this.raio;
    }
}
const circulo = new Circulo(5);
console.log("Área:", circulo.calcularArea());
console.log("Perimetro:", circulo.calcularPerimetro());