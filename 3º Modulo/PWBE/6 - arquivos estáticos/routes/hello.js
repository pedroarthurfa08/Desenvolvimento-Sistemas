// Todas as rotas devem ser definidas neste arquivo.

const express = require('express')
// Importa a mini aplicação de roteamento do express.
const router = express.Router()

/* -----  Roteamentos ----- */

router.get('/', (req, res) => {
    res.send('Hello World!')
})

router.get('/ola_form', (req, res) => {
    res.render('ola_form')
})

router.post('/ola', (req, res) => {
    // req.body é um objeto que contém os dados enviados no corpo da requisição
    nome = req.body.nome // recupera o valor do parametro com chave = nome
    res.render('ola_resposta', {nome: nome}) // renderiza a view ola_resposta.ejs e passa o valor do nome através de um objeto javascript
})

/* -----  Fim dos roteamentos ----- */

// Exporta o roteador para ser utilizado em outros arquivos.
module.exports = router