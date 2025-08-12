
const Operacao = require('../models/operacao')


exports.save = function (req, res) {
    if (!req.session.user) {
        return res.status(401).send('Usuário não autenticado.');
    }
    /* Criar uma nova instância da classe Operacao com os dados recebidos do corpo da requisição */
    const operacao = new Operacao(req.body)
    /* Validar e realizar as conversoes necessarias nos dados da classe */
    operacao.validate()
    if (operacao.errors.length > 0) {
        return res.send(operacao.errors)
    } else {
        const usuario_id = req.session.user.id;
        operacao.create(usuario_id)
            .then((result) => {
                //res.redirect('/operacoes')
                res.send('Operação salva com sucesso com o id: ' + result)
            })
            .catch((error) => {
                res.status(500).send(error)
            })
    }
}