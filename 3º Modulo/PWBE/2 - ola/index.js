const express = require('express')
const app = express()
const port = 3000

app.set('views', 'views')

app.set('view engine', 'ejs')

app.use(express.urlencoded({extended: false}))

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/ola_form',(req, res) => {
    res.render('ola_form')
})

app.post('/ola', (req, res) => {
    const nome = req.body.nome
    res.render('ola_resposta', {nome: nome})
})

app.listen(port, () => {
  console.log(`Example app listening on http://localhost:${port}`)
})
