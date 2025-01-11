document.getElementById("inputText").addEventListener("keyup", function () {
    const inputText = this.value;
    document.getElementById("outputText").value = inputText;
  });
  