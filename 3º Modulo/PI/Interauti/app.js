const express = require('express');
const cookieParser = require('cookie-parser');
const path = require('path');
const { auth } = require('./middleware/auth');
const methodOverride = require('method-override');
const populateUserOptional = require('./middleware/populateUserOptional');
const app = express();
const pool = require('./config/database'); // Garante conexão PostgreSQL

// Configurações
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middlewares
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(methodOverride('_method'));
app.use(express.static(path.join(__dirname, 'public')));
app.use(populateUserOptional);

// Rotas
authRoutes = require('./routes/auth');
taskRoutes = require('./routes/tasks');
contatoRoutes = require('./routes/contato');
sobreRoutes = require('./routes/sobre');
dashboardRoutes = require('./routes/dashboard');
agendaRoutes = require('./routes/agenda');
app.use('/', authRoutes);
app.use('/tasks', auth, taskRoutes);
app.use('/', contatoRoutes);
app.use('/', sobreRoutes);
app.use('/', dashboardRoutes);
app.use('/', agendaRoutes);

// Tratamento de erros
app.use((err, req, res, next) => {
    console.error('Erro:', err);
    res.status(500).render('error', {
        message: process.env.NODE_ENV === 'production' 
            ? 'Ocorreu um erro interno. Por favor, tente novamente mais tarde.'
            : err.message
    });
});

// Inicia o servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
    console.log(`Acesse: http://localhost:${PORT}/login`);
});

module.exports = app; 