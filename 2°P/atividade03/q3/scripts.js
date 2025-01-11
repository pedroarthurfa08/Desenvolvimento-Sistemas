function converterParaFahrenheit() {
    const temperaturaCelsius = parseFloat(document.getElementById('temperatura-celsius').value);
    const temperaturaFahrenheit = (temperaturaCelsius * 9/5) + 32;
    
    document.getElementById('resultado').innerHTML = `${temperaturaCelsius}°C é igual a ${temperaturaFahrenheit}°F`;
   }