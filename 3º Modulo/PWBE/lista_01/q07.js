const n = parseInt(prompt("Digite um número inteiro positivo:"));

if (n > 0) {
    console.log(`Tabuada de ${n}:`);
    for (let i = 1; i <= 10; i++) {
        console.log(`${n} x ${i} = ${n * i}`);
    }
} else {
    console.log("Por favor, digite um número inteiro positivo.");
}
