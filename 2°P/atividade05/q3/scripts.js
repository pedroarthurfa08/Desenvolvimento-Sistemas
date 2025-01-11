document.getElementById('alterarModo').addEventListener('click', function () {
  const hora = parseInt(document.getElementById('horaInput').value);
  if (isNaN(hora) || hora < 0 || hora > 23) {
    alert("Por favor, insira um número válido entre 0 e 23.");
    return;
  }
  if (hora >= 18 || hora < 6) {
    document.body.style.backgroundColor = "black";
    document.body.style.color = "white";
  } else {
    document.body.style.backgroundColor = "white";
    document.body.style.color = "black";
  }
});