const jwt = require('jsonwebtoken');
const User = require('../models/User');

const auth = async (req, res, next) => {
    try {
        // Verificar token no cookie
        const token = req.cookies.token;
        if (!token) {
            console.log('Token não encontrado nos cookies');
            return res.redirect('/login');
        }

        // Verificar token
        const decoded = jwt.verify(token, process.env.JWT_SECRET || 'seu_segredo_jwt');
        console.log('Token decodificado:', decoded);
        
        // Buscar usuário
        const user = await User.findById(decoded.userId);
        if (!user) {
            console.log('Usuário não encontrado:', decoded.userId);
            res.clearCookie('token');
            return res.redirect('/login');
        }

        // Converter photo_url para photoUrl para compatibilidade com a view
        if (user.photo_url) {
            user.photoUrl = user.photo_url;
        }

        // Adicionar usuário ao request
        req.user = user;
        console.log('Usuário autenticado:', user.email);
        next();
    } catch (error) {
        console.error('Erro de autenticação:', error);
        res.clearCookie('token');
        res.redirect('/login');
    }
};

// Middleware para verificar se é admin
const isAdmin = (req, res, next) => {
    if (req.user && req.user.role === 'admin') {
        next();
    } else {
        res.status(403).render('error', { message: 'Acesso negado' });
    }
};

// Middleware para rotas públicas (não autenticadas)
const isNotAuthenticated = (req, res, next) => {
    if (req.cookies && req.cookies.token) {
        // Usuário já autenticado, redireciona para /tasks
        return res.redirect('/tasks');
    }
    next();
};

module.exports = { auth, isAdmin, isNotAuthenticated }; 