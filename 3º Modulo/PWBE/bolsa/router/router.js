const express = require('express')
const router = express.Router()

const listFaturamento = []

router.get('/bolsa_form', (req, res) =>{
  res.render('bolsa_form')
})

router.post('/bolsa_resposta', (req, res) => {
  const codigo = req.body.codigo
  const data = req.body.data
  const quantidade = parseInt(req.body.quantidade)
  const preco = parseFloat(req.body.preco)
  const tipo = req.body.tipo

  const valorBruto = quantidade * preco
  let valorLiquido

  if (tipo.toLowerCase() === 'compra') {
    valorLiquido = valorBruto + (valorBruto * 0.005)
  } else if (tipo.toLowerCase() === 'venda') {
    valorLiquido = valorBruto - (valorBruto * 0.005)
  }

  const elementos = [codigo, data, tipo, quantidade, preco, valorBruto, valorLiquido]

  listFaturamento.push(elementos)

  res.render('bolsa_resposta', {
    listFaturamento: listFaturamento
  })
})

module.exports = router