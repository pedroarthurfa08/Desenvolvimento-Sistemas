// Função para confirmar exclusão
function confirmDelete(id) {
    if (confirm('Tem certeza que deseja excluir esta tarefa?')) {
        document.getElementById(`delete-form-${id}`).submit();
    }
}

// Função para marcar tarefa como concluída
function toggleComplete(id) {
    document.getElementById(`complete-form-${id}`).submit();
}

// Função para mostrar/esconder descrição
function toggleDescription(id) {
    const description = document.getElementById(`description-${id}`);
    const button = document.getElementById(`toggle-description-${id}`);
    
    if (description.style.display === 'none') {
        description.style.display = 'block';
        button.innerHTML = '<i class="fas fa-chevron-up"></i> Esconder';
    } else {
        description.style.display = 'none';
        button.innerHTML = '<i class="fas fa-chevron-down"></i> Mostrar';
    }
}

// Função para validar formulários
function validateForm(formId) {
    const form = document.getElementById(formId);
    const title = form.querySelector('input[name="title"]');
    const description = form.querySelector('textarea[name="description"]');
    const dueDate = form.querySelector('input[name="dueDate"]');
    
    let isValid = true;
    
    // Validação do título
    if (title.value.trim().length < 3) {
        title.classList.add('is-invalid');
        isValid = false;
    } else {
        title.classList.remove('is-invalid');
    }
    
    // Validação da descrição
    if (description.value.trim().length > 500) {
        description.classList.add('is-invalid');
        isValid = false;
    } else {
        description.classList.remove('is-invalid');
    }
    
    // Validação da data
    if (dueDate.value) {
        const selectedDate = new Date(dueDate.value);
        const today = new Date();
        
        if (selectedDate <= today) {
            dueDate.classList.add('is-invalid');
            isValid = false;
        } else {
            dueDate.classList.remove('is-invalid');
        }
    }
    
    return isValid;
}

// Adiciona validação aos formulários
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this.id)) {
                e.preventDefault();
            }
        });
    });

    // Edição rápida de tarefa

    // Botão de edição rápida
    document.querySelectorAll('.quick-edit-task').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const taskId = this.getAttribute('data-task-id');
            fetch(`/tasks/${taskId}/json`)
                .then(res => res.json())
                .then(task => {
                    document.getElementById('editTaskId').value = task._id || task.id;
                    document.getElementById('editTitle').value = task.title;
                    document.getElementById('editDescription').value = task.description || '';
                    document.getElementById('editPriority').value = task.priority || 'média';
                    document.getElementById('editDate').value = task.date ? task.date.substr(0,10) : '';
                    document.getElementById('editTaskModal').style.display = 'flex';
                });
        });
    });

    // Fechar modal
    document.getElementById('closeEditModal').onclick = function() {
        document.getElementById('editTaskModal').style.display = 'none';
    };

    // Submeter edição rápida
    document.getElementById('editTaskForm').onsubmit = function(e) {
        e.preventDefault();
        const id = document.getElementById('editTaskId').value;
        const data = {
            title: document.getElementById('editTitle').value,
            description: document.getElementById('editDescription').value,
            priority: document.getElementById('editPriority').value,
            date: document.getElementById('editDate').value
        };
        fetch(`/tasks/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(res => {
            if (res.ok) {
                document.getElementById('editTaskModal').style.display = 'none';
                location.reload();
            } else {
                alert('Erro ao atualizar tarefa');
            }
        });
    };
}); 