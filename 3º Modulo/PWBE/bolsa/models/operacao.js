const validator = require('validator');
const TIPOS_VALIDOS = ['compra', 'venda'];

const pool = require('../db/postgres');

/**
 * Classe para representar uma operação da bolsa de valores.
 * @ param { object } data Objecto javascript (chave: valor) com parâmetros da requisição.
 * @ param { string } errors Array de mensagens de erro de validação de propriedades da classe.
 */
class Operacao {
	constructor(data) {
		this.data = data;
		this.errors = [];
	}
}

Operacao.prototype.validate = function () {
	let data = this.data.data;
	let ativo = this.data.ativo;
	let tipoDeOperacao = this.data.tipoDeOperacao;
	let quantidade = this.data.quantidade;
	let preco = this.data.preco;

	if (!validator.isDate(data)) {
		this.errors.push('Formato de data inválido.')
	}
	// Validação por regex para o código do ativo
	if (!/^[A-Z]{4}\d{1,2}$/.test(ativo)) {
		this.errors.push('Código do ativo inválido.')
	}
	if (!validator.isIn(tipoDeOperacao, TIPOS_VALIDOS)) {
		this.errors.push('Tipo de operação inválido.')
	}
	if (!validator.isInt(quantidade)) {
		this.errors.push('Quantidade deve ser um número inteiro.')
	} else {
		quantidade = parseInt(quantidade)
		if (quantidade <= 0) {
			this.errors.push('Quantidade deve ser maior que zero.')
		}
	}
	if (!validator.isFloat(preco)) {
		this.errors.push('Preço deve ser um número real.')
	} else {
		preco = parseFloat(preco)
		if (preco <= 0) {
			this.errors.push('Preço deve ser maior que zero.')
		}
	}

	// Corrigir: garantir que quantidade e preco são números antes do cálculo
	if (this.errors.length === 0) {
		quantidade = Number(quantidade);
		preco = Number(preco);
		const valorBruto = preco * quantidade;
		const taxaB3 = valorBruto * 0.0003; // 0.03% de taxa B3
		const valorLiquido = tipoDeOperacao === 'compra' ? (valorBruto + taxaB3) : (valorBruto - taxaB3);
		validatedData = {
			data: data,
			ativo: ativo,
			tipoDeOperacao: tipoDeOperacao,
			quantidade: quantidade,
			preco: preco,
			valorBruto: valorBruto,
			taxaB3: taxaB3,
			valorLiquido: valorLiquido
		}
		this.data = validatedData;
		console.log('Operação validada:', this.data);
	}
}

Operacao.prototype.create = function (usuario_id) {
    const query_text = 'INSERT INTO operacoes (data, ativo, tipo_de_operacao, quantidade, preco, valor_bruto, taxa_b3, valor_liquido, usuario_id) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9) RETURNING id;'
    const query_params = [this.data.data, this.data.ativo, this.data.tipoDeOperacao, this.data.quantidade, this.data.preco, this.data.valorBruto, this.data.taxaB3, this.data.valorLiquido, usuario_id]
    return new Promise((resolve, reject) => {
        pool.query(query_text, query_params, (error, result) => {
            if (error) {
                reject('Erro ao inserir operação: ' + error);
            } else {
                const idDaOperacaoSalva = result.rows[0].id;
                resolve(idDaOperacaoSalva);
            }
        });
    })
}

Operacao.readAllByUser = function (usuario_id) {
    return new Promise((resolve, reject) => {
        const query = 'SELECT * FROM operacoes WHERE usuario_id = $1';
        pool.query(query, [usuario_id], (error, result) => {
            if (error) {
                reject('Erro ao buscar operações: ' + error);
            } else {
                // Mapeia os campos para camelCase para compatibilidade com a view
                const operacoes = result.rows.map(op => ({
                    ...op,
                    tipoDeOperacao: op.tipo_de_operacao,
                    valorBruto: op.valor_bruto,
                    taxaB3: op.taxa_b3,
                    valorLiquido: op.valor_liquido
                }));
                resolve(operacoes);
            }
        });
    });
}

Operacao.readAllByUserAndAtivo = function (usuario_id, ativo) {
    return new Promise((resolve, reject) => {
        const query = 'SELECT * FROM operacoes WHERE usuario_id = $1 AND ativo = $2';
        pool.query(query, [usuario_id, ativo], (error, result) => {
            if (error) {
                reject('Erro ao buscar operações: ' + error);
            } else {
                const operacoes = result.rows.map(op => ({
                    ...op,
                    tipoDeOperacao: op.tipo_de_operacao,
                    valorBruto: op.valor_bruto,
                    taxaB3: op.taxa_b3,
                    valorLiquido: op.valor_liquido
                }));
                resolve(operacoes);
            }
        });
    });
}

Operacao.prototype.update = function (id, usuario_id) {
    return new Promise((resolve, reject) => {
        // Recalcula os valores
        let quantidade = Number(this.data.quantidade);
        let preco = Number(this.data.preco);
        const valorBruto = preco * quantidade;
        const taxaB3 = valorBruto * 0.0003;
        const valorLiquido = this.data.tipoDeOperacao === 'compra' ? (valorBruto + taxaB3) : (valorBruto - taxaB3);
        const query = `UPDATE operacoes SET data = $1, ativo = $2, tipo_de_operacao = $3, quantidade = $4, preco = $5, valor_bruto = $6, taxa_b3 = $7, valor_liquido = $8 WHERE id = $9 AND usuario_id = $10`;
        const params = [this.data.data, this.data.ativo, this.data.tipoDeOperacao, quantidade, preco, valorBruto, taxaB3, valorLiquido, id, usuario_id];
        pool.query(query, params, (error, result) => {
            if (error) {
                reject('Erro ao atualizar operação: ' + error);
            } else {
                resolve();
            }
        });
    });
}

Operacao.delete = function (id, usuario_id) {
    return new Promise((resolve, reject) => {
        const query = 'DELETE FROM operacoes WHERE id = $1 AND usuario_id = $2';
        pool.query(query, [id, usuario_id], (error, result) => {
            if (error) {
                reject('Erro ao excluir operação: ' + error);
            } else {
                resolve();
            }
        });
    });
}

module.exports = Operacao;