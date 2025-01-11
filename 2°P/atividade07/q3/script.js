function moveOption(fromSelectId, toSelectId) {
    const fromSelect = document.getElementById(fromSelectId);
    const toSelect = document.getElementById(toSelectId);

    const selectedOption = fromSelect.options[fromSelect.selectedIndex];
    if (selectedOption) {
        const newOption = document.createElement('option');
        newOption.value = selectedOption.value;
        newOption.text = selectedOption.text;
        toSelect.add(newOption);

        fromSelect.remove(fromSelect.selectedIndex);
    } else {
        alert('Por favor, selecione uma opção para mover.');
    }
}

document.getElementById('moveToRight').addEventListener('click', function() {
    moveOption('select1', 'select2');
});

document.getElementById('moveToLeft').addEventListener('click', function() {
    moveOption('select2', 'select1');
});