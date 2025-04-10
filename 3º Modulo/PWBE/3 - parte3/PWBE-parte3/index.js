const express = require('express')
const app = express()
const port = 3000

app.use(express.urlencoded({extend: false}))

app.set('viwes', 'views')

app.set('view engine', 'ejs')

app.get('/ola_form', (req, res) => {
    res.render('ola_form')
})

app.post('/ola', (req, res) => {
    nome = req.body.nome
    res.send(`Olá ${nome}`)
})

app.listen(port, () => {
  console.log(`Example app listening on http://localhost:${port}`)
})