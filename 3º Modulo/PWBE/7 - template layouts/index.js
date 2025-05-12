const express = require('express')
const app = express()
const port = 3000

/* O express-ejs-layouts é um middleware para o Express que permite 
a reutilização de templates com layouts EJS. */
const expressLayouts = require('express-ejs-layouts')

const mainRouter = require('./routes/main-router')
const operacaoRouter = require('./routes/operacao-router')

/* Definie o local onde estão localizadas as views do projeto */
app.set('views', 'views')
/* Define o template engine que será utilizado para renderizar as views */
// O EJS é um template engine que permite criar views dinâmicas utilizando JavaScript
app.set('view engine', 'ejs')

// Importa o express-ejs-layouts para utilizar layouts para reutilização nas views
app.use(expressLayouts);

/* Middleware para servir arquivos estáticos, como CSS e JavaScript */
app.use(express.static('public'))

/*
body-parser é Middleware para fazer o parse do corpo da requisição antes de utilizarmos o req.body
O express.urlencoded() faz o parse do corpo da requisição para o formato URL-encoded.
O valor falso para extended indica que o body-parser vai aceitar somente strings e arrays, enquanto
o valor verdadeiro indica que o body-parser vai aceitar objetos aninhados ou qualquer outro tipo.
*/
app.use(express.urlencoded({extended: false}))

/* Definir que o objeto app, agora direcione todas as 
requisições para a raiz de requisições para o objeto router. */
app.use('/', mainRouter)
app.use('/operacao', operacaoRouter)

// O método listen() inicia o servidor e escuta as requisições na porta definida.
app.listen(port, () => {
    console.log(`Example app listening on port http://localhost:${port}`)
})