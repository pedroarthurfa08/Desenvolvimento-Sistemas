const express = require('express')
const app = express()
const port = 3000

// roteamentos
const router = require('./routes/router')

/* Importa o express-ejs-layouts para o EJS que permite usar layouts
 para reaproveitamento de templates em views EJS */
const expressLayouts = require('express-ejs-layouts')

/* Definie o local onde estão localizadas as views do projeto */
app.set('views', 'views')
/* Define o template engine que será utilizado para renderizar as views */
// O EJS é um template engine que permite criar views dinâmicas utilizando JavaScript
app.set('view engine', 'ejs')

/* Define o layout de reaproveitamento de templates padrão que 
será utilizado para renderizar as views */
app.use(expressLayouts);

/* Define o local onde estão localizados os arquivos estáticos do projeto */
app.use(express.static('public'))

/*
body-parser é Middleware para fazer o parse do corpo da requisição antes de utilizarmos o req.body
O express.urlencoded() faz o parse do corpo da requisição para o formato URL-encoded.
O valor falso para extended indica que o body-parser vai aceitar somente strings e arrays, enquanto
o valor verdadeiro indica que o body-parser vai aceitar objetos aninhados ou qualquer outro tipo.
*/
app.use(express.urlencoded({ extended: false }))

const session = require('express-session')
app.use(session({
    secret: 'segredo_super_secreto',
    resave: false,
    saveUninitialized: false,
    cookie: { maxAge: 1000 * 60 * 60 } // 1 hora
}))

app.use('/', router)

app.listen(port, () => {
    console.log(`Example app listening on http://localhost:${port}/login`)
})