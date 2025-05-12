var express = require('express');
var router = express.Router();

const operacaoController = require('../controllers/operacao-controller.js');

// funcoes de roteamento relativos às operacoes ficam aqui.
router.get('/operacoes', function (req, res, next) {
    res.render('pages/operacoes',
        {
            title: 'Operações',
            paginaAtiva: 'operacoes',
            operacoes: operacaoController.listaDeOperacoes
        }
    );
});

router.get('/nova_operacao', function (req, res, next) {
    res.render('pages/nova_operacao',
        {
            title: 'Nova Operação',
            paginaAtiva: 'operacoes'
        }
    );
});

router.post('/salvar_operacao', operacaoController.salvarOperacao);

module.exports = router;