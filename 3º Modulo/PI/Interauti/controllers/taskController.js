const Task = require('../models/Task');

const taskController = {
    index: async (req, res) => {
        try {
            const page = parseInt(req.query.page) || 1;
            const limit = parseInt(req.query.limit) || 10;
            const skip = (page - 1) * limit;

            // Filtros
            const filters = {};
            if (req.query.status) filters.status = req.query.status;
            if (req.query.priority) filters.priority = req.query.priority;

            // Busca todas as tarefas do usuário com filtros
            let tasks = await Task.findAllByUser(req.user.id, filters);
            const total = tasks.length;
            const totalPages = Math.ceil(total / limit);
            const hasNextPage = page < totalPages;
            const hasPrevPage = page > 1;
            // Paginação manual
            tasks = tasks.slice(skip, skip + limit);

            res.render('tasks/index', {
                tasks,
                pagination: {
                    page,
                    limit,
                    total,
                    totalPages,
                    hasNextPage,
                    hasPrevPage
                },
                filters: {
                    status: req.query.status,
                    priority: req.query.priority
                },
                user: req.user
            });
        } catch (error) {
            console.error('Erro ao buscar tarefas:', error);
            res.status(500).render('error', { message: 'Erro ao carregar tarefas' });
        }
    },

    create: (req, res) => {
        res.render('tasks/create', { user: req.user });
    },

    store: async (req, res) => {
        try {
            const { title, description, priority, date, time, duration } = req.body;
            const sanitizedData = {
                title: title.trim(),
                description: description ? description.trim() : '',
                priority: priority || 'média',
                date: date || null,
                time: time || null,
                duration: duration ? parseInt(duration) : null,
                user_id: req.user.id,
                tags: Array.isArray(req.body.tags) ? req.body.tags : (req.body.tags ? [req.body.tags] : []),
                status: 'pendente',
                deleted: false
            };
            await Task.create(sanitizedData);
            res.redirect('/tasks');
        } catch (error) {
            console.error('Erro ao criar tarefa:', error);
            res.status(500).render('error', { message: 'Erro ao criar tarefa' });
        }
    },

    edit: async (req, res) => {
        try {
            const task = await Task.findById(req.params.id);
            if (!task || task.user_id !== req.user.id) {
                return res.status(404).render('error', { message: 'Tarefa não encontrada' });
            }
            res.render('tasks/edit', { task, user: req.user });
        } catch (error) {
            console.error('Erro ao buscar tarefa:', error);
            res.status(500).render('error', { message: 'Erro ao buscar tarefa' });
        }
    },

    update: async (req, res) => {
        try {
            const task = await Task.findById(req.params.id);
            if (!task || task.user_id !== req.user.id) {
                if (req.headers['content-type'] && req.headers['content-type'].includes('application/json')) {
                    return res.status(404).json({ error: 'Tarefa não encontrada' });
                }
                return res.status(404).render('error', { message: 'Tarefa não encontrada' });
            }
            const { title, description, priority, date, time, duration, status, tags } = req.body;
            await Task.update(req.params.id, {
                title: title.trim(),
                description: description ? description.trim() : '',
                priority,
                date,
                time,
                duration: duration ? parseInt(duration) : null,
                status,
                tags: Array.isArray(tags) ? tags : (tags ? [tags] : [])
            });
            if (req.headers['content-type'] && req.headers['content-type'].includes('application/json')) {
                return res.json({ success: true });
            }
            res.redirect('/tasks');
        } catch (error) {
            console.error('Erro ao atualizar tarefa:', error);
            if (req.headers['content-type'] && req.headers['content-type'].includes('application/json')) {
                return res.status(500).json({ error: 'Erro ao atualizar tarefa' });
            }
            res.status(500).render('error', { message: 'Erro ao atualizar tarefa' });
        }
    },

    delete: async (req, res) => {
        try {
            const task = await Task.findById(req.params.id);
            if (!task || task.user_id !== req.user.id) {
                return res.status(404).render('error', { message: 'Tarefa não encontrada' });
            }
            await Task.delete(req.params.id);
            res.redirect('/tasks');
        } catch (error) {
            console.error('Erro ao deletar tarefa:', error);
            res.status(500).render('error', { message: 'Erro ao deletar tarefa' });
        }
    },

    show: async (req, res) => {
        try {
            console.log('Buscando tarefa id:', req.params.id, 'para usuário:', req.user.id);
            const task = await Task.findById(req.params.id);
            console.log('Tarefa encontrada:', task);
            if (!task || task.user_id !== req.user.id) {
                return res.status(404).render('error', { message: 'Tarefa não encontrada' });
            }
            res.render('tasks/show', { task, user: req.user });
        } catch (error) {
            console.error('Erro ao exibir tarefa:', error);
            res.status(500).render('error', { message: 'Erro ao exibir tarefa' });
        }
    },

    dashboard: async (req, res) => {
        try {
            const stats = await Task.getDashboardStats(req.user.id);
            // Buscar tarefas abertas (não deletadas)
            const allTasks = await Task.findAllByUser(req.user.id);
            res.render('dashboard', { stats, tasks: allTasks, user: req.user });
        } catch (error) {
            console.error('Erro ao carregar dashboard:', error);
            res.status(500).render('error', { message: 'Erro ao carregar dashboard' });
        }
    }
};

module.exports = taskController; 