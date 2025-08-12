const express = require('express')
const router = express.Router()

const operacaoController = require('../controllers/operacao-controller')
const authController = require('../controllers/auth-controller')
const Operacao = require('../models/operacao')


function requireLogin(req, res, next) {
  if (!req.session.user) {
    return res.redirect('/login');
  }
  next();
}

router.use(function(req, res, next) {
  res.locals.user = req.session.user;
  next();
});

/* ----- funções de roteamento ----- */
router.get('/', function (req, res) {
  res.render('pages/home',
    {
      title: 'Home',
      paginaAtiva: 'home'
    }
  );
});

router.get('/nova_operacao', function (req, res) {
  res.render('pages/nova_operacao',
    {
      title: 'Nova Operação',
      paginaAtiva: 'operacao'
    }
  );
})

router.get('/operacoes', requireLogin, async function (req, res) {
  try {
    const operacoes = await Operacao.readAllByUser(req.session.user.id);
    res.render('pages/operacoes', {
      title: 'Operações',
      paginaAtiva: 'operacao',
      operacoes
    });
  } catch (err) {
    res.status(500).send('Erro ao buscar operações: ' + err);
  }
})

router.get('/operacoes/:id/editar', requireLogin, async function (req, res) {
  const Operacao = require('../models/operacao');
  const id = req.params.id;
  const usuario_id = req.session.user.id;
  const operacoes = await Operacao.readAllByUser(usuario_id);
  const operacao = operacoes.find(op => op.id == id);
  if (!operacao) {
    return res.status(404).send('Operação não encontrada.');
  }
  res.render('pages/editar_operacao', {
    title: 'Editar Operação',
    paginaAtiva: 'operacao',
    operacao
  });
});

// Rota para atualizar operação
router.post('/operacoes/:id/editar', requireLogin, async function (req, res) {
  const Operacao = require('../models/operacao');
  const id = req.params.id;
  const usuario_id = req.session.user.id;
  const operacao = new Operacao(req.body);
  operacao.validate();
  if (operacao.errors.length > 0) {
    return res.send(operacao.errors);
  }
  await operacao.update(id, usuario_id);
  res.redirect('/operacoes');
});

// Rota para excluir operação
router.post('/operacoes/:id/excluir', requireLogin, async function (req, res) {
  const Operacao = require('../models/operacao');
  const id = req.params.id;
  const usuario_id = req.session.user.id;
  await Operacao.delete(id, usuario_id);
  res.redirect('/operacoes');
});

// Rota para filtrar operações por ativo
router.get('/operacoes/ativo/:ativo', requireLogin, async function (req, res) {
  const Operacao = require('../models/operacao');
  const usuario_id = req.session.user.id;
  const ativo = req.params.ativo;
  const operacoes = await Operacao.readAllByUserAndAtivo(usuario_id, ativo);
  res.render('pages/operacoes', {
    title: 'Operações',
    paginaAtiva: 'operacao',
    operacoes
  });
});

router.get('/login', function (req, res) {
  res.render('pages/login', {
    title: 'Login',
    paginaAtiva: ''
  });
});

router.get('/register', function (req, res) {
  res.render('pages/register', {
    title: 'Registro',
    paginaAtiva: ''
  });
});

router.get('/logout', function (req, res) {
  req.session.destroy(() => {
    res.redirect('/login');
  });
});


router.post('/salvar_operacao', requireLogin, operacaoController.save)
router.post('/register', authController.register)
router.post('/login', authController.login)


module.exports = router