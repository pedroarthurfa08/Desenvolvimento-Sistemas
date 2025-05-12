operacoes = [];

exports.salvarOperacao = function (req, res) {
    // recuperar dados da operacao e salvar.
    let data = req.body.data
    let ativo = req.body.ativo
    let tipoDeOperacao = req.body.tipoDeOperacao
    let quantidade = req.body.quantidade
    let preco = req.body.preco
    // valores derivados
    let valorBruto = parseInt(quantidade) * parseFloat(preco)
    let taxaB3 = 0.0003 * valorBruto
    let valorLiquido = null
    if (tipoDeOperacao == 'compra') {
        valorLiquido = valorBruto + taxaB3
    } else {
        valorLiquido = valorBruto - taxaB3
    }
    let operacao = {
        data: data,
        ativo: ativo,
        tipoDeOperacao: tipoDeOperacao,
        quantidade: quantidade,
        preco: preco,
        valorBruto: valorBruto,
        taxaB3: taxaB3,
        valorLiquido: valorLiquido
    }
    operacoes.push(operacao)
    res.redirect('/operacao/operacoes')
}

module.exports.operacoes = operacoes;