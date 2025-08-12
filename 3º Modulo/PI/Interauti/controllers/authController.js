const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const fs = require('fs');
const path = require('path');

// Renderiza a página de login
exports.getLogin = (req, res) => {
    res.render('auth/login', { error: null, user: null });
};

// Renderiza a página de registro
exports.getRegister = (req, res) => {
    res.render('auth/register', { error: null, user: null });
};

// Processa o login
exports.postLogin = async (req, res) => {
    try {
        const { email, password } = req.body;
        console.log('Tentativa de login para:', email);

        // Busca o usuário pelo email
        const user = await User.findByEmail(email);
        if (!user) {
            console.log('Usuário não encontrado:', email);
            return res.render('auth/login', {
                error: 'Email ou senha inválidos',
                user: null
            });
        }

        console.log('Usuário encontrado, verificando senha...');

        // Verifica a senha usando o método do modelo
        const isValidPassword = await User.comparePassword(password, user.password);
        console.log('Resultado da verificação da senha:', isValidPassword);

        if (!isValidPassword) {
            console.log('Senha inválida para:', email);
            return res.render('auth/login', {
                error: 'Email ou senha inválidos',
                user: null
            });
        }

        // Gera o token JWT
        const token = jwt.sign(
            { userId: user.id },
            process.env.JWT_SECRET || 'seu_segredo_jwt',
            { expiresIn: '24h' }
        );

        console.log('Token gerado para:', email);

        // Define o cookie com o token
        res.cookie('token', token, {
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production',
            maxAge: 24 * 60 * 60 * 1000 // 24 horas
        });

        console.log('Login bem-sucedido para:', email);
        res.redirect('/tasks');
    } catch (error) {
        console.error('Erro no login:', error);
        res.render('auth/login', {
            error: 'Ocorreu um erro ao fazer login. Tente novamente.'
        });
    }
};

// Processa o registro
exports.postRegister = async (req, res) => {
    try {
        const { name, email, password } = req.body;
        console.log('Tentativa de registro para:', email);

        // Verifica se o email já está em uso
        const existingUser = await User.findByEmail(email);
        if (existingUser) {
            console.log('Email já em uso:', email);
            return res.render('auth/register', {
                error: 'Este email já está em uso',
                user: null
            });
        }

        // Cria o novo usuário
        const user = await User.create({ name, email, password });
        console.log('Usuário registrado com sucesso:', email);

        // Redireciona para o login
        res.redirect('/login');
    } catch (error) {
        console.error('Erro no registro:', error);
        res.render('auth/register', {
            error: 'Ocorreu um erro ao criar sua conta. Tente novamente.',
            user: null
        });
    }
};

// Processa o logout
exports.logout = (req, res) => {
    console.log('Logout realizado');
    res.clearCookie('token');
    res.redirect('/login');
};

// Upload de foto de perfil
exports.uploadPhoto = async (req, res) => {
    try {
        if (!req.file) {
            return res.redirect('/profile?error=Selecione uma imagem válida.');
        }
        // Atualiza o caminho da foto no banco
        const photoUrl = '/images/profiles/' + req.file.filename;
        await User.updatePhoto(req.user.id, photoUrl);
        // Atualiza o objeto user na sessão (se aplicável)
        req.user.photoUrl = photoUrl;
        res.redirect('/profile?success=Foto atualizada com sucesso!');
    } catch (error) {
        console.error('Erro ao fazer upload da foto:', error);
        res.redirect('/profile?error=Erro ao atualizar foto.');
    }
};

exports.updateProfile = async (req, res) => {
    try {
        console.log('Iniciando atualização do perfil para usuário:', req.user.id);
        console.log('Dados recebidos:', req.body);
        
        const { name, email, theme, notifications, language } = req.body;
        
        // Validação básica
        if (!name || !email) {
            console.log('Dados obrigatórios faltando');
            return res.redirect('/profile?error=Nome e email são obrigatórios.');
        }
        
        // Verificar se o email já está em uso por outro usuário
        const existingUser = await User.findByEmail(email);
        if (existingUser && existingUser.id !== req.user.id) {
            console.log('Email já em uso por outro usuário');
            return res.redirect('/profile?error=Este email já está em uso por outro usuário.');
        }
        
        const settings = {
            theme: theme || 'dark',
            notifications: !!notifications,
            language: language || 'pt-BR'
        };
        
        console.log('Atualizando perfil com settings:', settings);
        
        // Atualizar o usuário no banco de dados
        await User.updateProfile(req.user.id, {
            name: name.trim(),
            email: email.trim(),
            settings
        });
        
        console.log('Perfil atualizado com sucesso');
        res.redirect('/profile?success=Perfil atualizado com sucesso!');
    } catch (error) {
        console.error('Erro ao atualizar perfil:', error);
        res.redirect('/profile?error=Erro ao atualizar perfil. Tente novamente.');
    }
}; 

exports.removePhoto = async (req, res) => {
    try {
        // Buscar o usuário para pegar o caminho da foto
        const user = await User.findById(req.user.id);
        if (user && user.photo_url) {
            // Caminho absoluto do arquivo
            const filePath = path.join(__dirname, '../public', user.photo_url);
            // Remover arquivo se existir
            if (fs.existsSync(filePath)) {
                fs.unlinkSync(filePath);
            }
        }
        // Atualizar o campo photo_url para NULL
        await User.updatePhoto(req.user.id, null);
        res.redirect('/profile?success=Foto removida com sucesso!');
    } catch (error) {
        console.error('Erro ao remover foto:', error);
        res.redirect('/profile?error=Erro ao remover foto.');
    }
}; 