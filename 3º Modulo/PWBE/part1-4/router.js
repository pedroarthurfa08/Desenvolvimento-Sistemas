const express = require('express')
const router = express.Router()

const listFaturamento = []

router.get('/', (req, res) => {
  res.send('Hello World!')
})

router.get('/ola_form',(req, res) => {
    res.render('ola_form')
})

router.post('/ola', (req, res) => {
    const nome = req.body.nome
    res.render('ola_resposta', {nome: nome})
})

router.get('/soma_form', (req, res) => {
  res.render('soma_form')
})

router.post("/soma", (req, res) => {
  const n1 = Number(req.body.numero1)
  const n2 = Number(req.body.numero2)
  const soma = n1 + n2

  res.render('soma_resposta',{soma: soma})
})

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

  res.render('resposta', {
    listFaturamento: listFaturamento
  })
})

module.exports = router