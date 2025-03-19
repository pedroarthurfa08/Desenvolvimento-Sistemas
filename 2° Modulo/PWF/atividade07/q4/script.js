let taskId = 1;

document.getElementById('addTaskButton').addEventListener('click', function() {
    const taskDescription = document.getElementById('taskDescription').value.trim();
    const taskCompletion = document.getElementById('taskCompletion').value;

    if (!taskDescription) {
        alert('Por favor, insira a descrição da tarefa.');
        return;
    }

    const tableBody = document.getElementById('taskTable').querySelector('tbody');

    const newRow = document.createElement('tr');

    const idCell = document.createElement('td');
    idCell.textContent = taskId++;

    const descriptionCell = document.createElement('td');
    descriptionCell.textContent = taskDescription;

    const completionCell = document.createElement('td');
    completionCell.textContent = `${taskCompletion}%`;

    newRow.appendChild(idCell);
    newRow.appendChild(descriptionCell);
    newRow.appendChild(completionCell);

    tableBody.appendChild(newRow);

    document.getElementById('taskDescription').value = '';
    document.getElementById('taskCompletion').value = '0';
});