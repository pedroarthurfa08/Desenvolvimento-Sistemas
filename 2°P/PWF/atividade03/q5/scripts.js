const origem = document.getElementById('origem');
const destino = document.getElementById('destino');

origem.addEventListener('keyup', function() {
  destino.value = origem.value;
});