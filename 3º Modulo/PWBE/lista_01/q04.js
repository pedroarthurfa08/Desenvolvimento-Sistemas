function calcularMedia(numeros) {
    if (numeros.lenght === 0) return 0;
    const soma = numeros.reduce((acc, num) => acc + num, 0);
    return soma / numeros.length;
}

const numeros = [1,2,3,4,5,6,7,8,9];
console.log(calcularMedia(numeros));