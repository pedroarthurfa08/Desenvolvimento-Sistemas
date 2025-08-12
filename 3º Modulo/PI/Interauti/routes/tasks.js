const express = require('express');
const router = express.Router();
const taskController = require('../controllers/taskController');
const { auth } = require('../middleware/auth');

// Middleware para debug
router.use((req, res, next) => {
    console.log('Rota de tarefas acessada:', req.method, req.path);
    console.log('Usuário autenticado:', req.user ? req.user.email : 'Não autenticado');
    next();
});

// Todas as rotas de tarefas agora requerem autenticação
router.use(auth);

// Rotas de tarefas
router.get('/', taskController.index);
router.get('/create', taskController.create);
router.post('/', taskController.store);
router.get('/:id/edit', taskController.edit);
router.get('/:id', taskController.show);
router.post('/:id/delete', taskController.delete);
router.put('/:id', taskController.update);
router.get('/:id/json', async (req, res) => {
    const taskController = require('../controllers/taskController');
    const Task = require('../models/Task');
    try {
        const task = await Task.findById(req.params.id);
        if (!task || task.user_id !== req.user.id) {
            return res.status(404).json({ error: 'Tarefa não encontrada' });
        }
        res.json(task);
    } catch (error) {
        res.status(500).json({ error: 'Erro ao buscar tarefa' });
    }
});

module.exports = router; 