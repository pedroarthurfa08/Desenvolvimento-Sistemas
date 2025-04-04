function ehPalindromo(palavra) {
    const normalizada = palavra.toLowerCase().replace(/[\s]/g, '');
    const invertida = normalizada.split('').reverse().join('');
    return normalizada === invertida;
}

console.log(ehPalindromo("arara")); ''
console.log(ehPalindromo("ovo"));   ''
console.log(ehPalindromo("palavra"));''
