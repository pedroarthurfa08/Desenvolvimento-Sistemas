const textInput = document.getElementById('textInput');

textInput.addEventListener('focus', () => {
    textInput.style.backgroundColor = '#ffffcc';
});
textInput.addEventListener('blur', () => {
    textInput.style.backgroundColor = ''; 
});