document.getElementById('generateButton').addEventListener('click', function() {
    const tagName = document.getElementById('tagName').value;
    const tagContent = document.getElementById('tagContent').value;

    if (!tagName.trim()) {
        alert('Por favor, insira um nome de tag válido.');
        return;
    }

    const newElement = document.createElement(tagName);

    newElement.innerHTML = tagContent;

    const container = document.getElementById('container');
    container.appendChild(newElement);

    document.getElementById('tagName').value = '';
    document.getElementById('tagContent').value = '';
});