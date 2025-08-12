CREATE TABLE operacoes(
    id SERIAL NOT NULL,
    "data" date NOT NULL,
    ativo varchar(6) NOT NULL,
    tipo_de_operacao varchar(10) NOT NULL,
    quantidade integer NOT NULL,
    preco numeric(12,2) NOT NULL,
    valor_bruto numeric(14,2) NOT NULL,
    taxa_b3 numeric(10,2) NOT NULL,
    valor_liquido numeric(14,2) NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT operacoes_preco_check CHECK ((preco >= (0)::numeric)),
    CONSTRAINT operacoes_quantidade_check CHECK ((quantidade > 0)),
    CONSTRAINT operacoes_taxa_b3_check CHECK ((taxa_b3 >= (0)::numeric)),
    CONSTRAINT operacoes_tipo_de_operacao_check CHECK (((tipo_de_operacao)::text = ANY ((ARRAY['compra'::character varying, 'venda'::character varying])::text[]))),
    CONSTRAINT operacoes_valor_bruto_check CHECK ((valor_bruto >= (0)::numeric)),
    CONSTRAINT operacoes_valor_liquido_check CHECK ((valor_liquido >= (0)::numeric))
);

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);