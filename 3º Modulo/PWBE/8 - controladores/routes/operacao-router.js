var express = require('express');
var router = express.Router();

const operacaoController = require('../controllers/operacaoController.js');

router.get('/operacoes', function (req, res, next) {
    console.log(operacaoController.operacoes);
    res.render('pages/operacoes',
        {
            title: 'Operações',
            paginaAtiva: 'operacoes',
            operacoes: operacaoController.operacoes
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

/* redireciona o roteamento para ser tratato pelo controlador */
router.post('/salvar_operacao', operacaoController.salvarOperacao);

module.exports = router;