const Usuario = require('../models/usuario');
const bcrypt = require('bcrypt');
const validator = require('validator');

exports.register = async function (req, res) {
    const { nome, email, senha } = req.body;
    let error = null;
    if (!nome || !email || !senha) {
        error = 'Preencha todos os campos.';
    } else if (!validator.isEmail(email)) {
        error = 'E-mail inválido.';
    } else if (senha.length < 6) {
        error = 'A senha deve ter pelo menos 6 caracteres.';
    } else if (nome.trim().length < 2) {
        error = 'O nome deve ter pelo menos 2 caracteres.';
    }
    if (error) {
        return res.render('pages/register', { title: 'Registro', paginaAtiva: 'register', error });
    }
    try {
        const existingUser = await Usuario.findByEmail(email);
        if (existingUser) {
            return res.render('pages/register', { title: 'Registro', paginaAtiva: 'register', error: 'E-mail já cadastrado.' });
        }
        const usuario = new Usuario({ nome, email, senha });
        await usuario.create();
        res.redirect('/login');
    } catch (err) {
        res.render('pages/register', { title: 'Registro', paginaAtiva: 'register', error: err });
    }
};

exports.login = async function (req, res) {
    const { email, senha } = req.body;
    if (!email || !senha) {
        return res.render('pages/login', { title: 'Login', paginaAtiva: 'login', error: 'Preencha todos os campos.' });
    }
    try {
        const user = await Usuario.findByEmail(email);
        if (!user) {
            return res.render('pages/login', { title: 'Login', paginaAtiva: 'login', error: 'Usuário não encontrado.' });
        }
        const senhaCorreta = await bcrypt.compare(senha, user.senha);
        if (!senhaCorreta) {
            return res.render('pages/login', { title: 'Login', paginaAtiva: 'login', error: 'Senha incorreta.' });
        }
        // Aqui você pode salvar o usuário na sessão futuramente
        req.session.user = { id: user.id, nome: user.nome, email: user.email };
        res.redirect('/operacoes');
    } catch (err) {
        res.render('pages/login', { title: 'Login', paginaAtiva: 'login', error: err });
    }
}; 