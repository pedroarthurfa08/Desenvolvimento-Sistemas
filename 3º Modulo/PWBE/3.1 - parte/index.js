const express = require('express')
const app = express()
const port = 3000

app.use(express.urlencoded({extended: false}))

app.set('viwes', 'views')

app.set('view engine', 'ejs')

app.get("/home_soma", (req, res) => {
  res.render("home_soma")
})

app.post("/soma", (req, res) => {
  const n1 = Number(req.body.numero1)
  const n2 = Number(req.body.numero2)
  const soma = n1 + n2
  res.render('resposta_soma', {soma: soma})
})

app.listen(port, () => {
  console.log(`Example app listening on http://localhost:${port}`)
})