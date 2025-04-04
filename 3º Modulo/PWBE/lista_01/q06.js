let popA = 80000;
let popB = 20000;

const taxaA = 0.03;
const taxaB = 0.015;

let anos = 0;

while (popB < popA){
    popA += popA * taxaA;
    popB += popB * taxaB;
    anos++;
}

console.log(`Serão necessários ${anos} anos para que a população de B alcance a população de A`);
