const express = require('express')
const app = express()
const port = 3000

app.use(express.urlencoded({extend: false}))

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.post('/ola', (req, res) => {
    nome = req.body.nome
    res.send(`Olá ${nome}`)
})

app.listen(port, () => {
  console.log(`Example app listening on http://localhost:${port}`)
})
