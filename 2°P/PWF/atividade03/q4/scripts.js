let data = new Date();
let dia = data.getDate();
let mes = data.getMonth() + 1; 
let ano = data.getFullYear();

let dataFormatada = `${dia.toString().padStart(2, '0')}/${mes.toString().padStart(2, '0')}/${ano}`;

document.getElementById('data-atual').innerHTML = dataFormatada;
