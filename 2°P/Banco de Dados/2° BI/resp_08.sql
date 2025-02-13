-- Questão 01: Encontrar o nome e valor de todos os produtos com preço superior a 10.0. --
select 	nome, preco 
from 	produtos
where 	preco >= 10;

-- Questão 02: Listar a data de todos os pedidos feitos por um cliente específico, identificado pelo cliente com id = 2. --
select 	data_pedido
from	pedidos
where 	id_cliente = 2;

-- Questão 03: Listar a quantidade de pedidos realizados pelo cliente com id = 3 --
select 	count(*)
from 	pedidos
where	id_cliente = 3;

-- Questão 04:  Listar o nome, quantidade e preço unitário dos produtos que foram comprados em um pedido específico (id_pedido = 1), com quantidade e preço unitário. --
select 	p.nome, pp.quantidade, pp.preco_unitario
from  	produtos p, pedidos_produtos pp
where	p.id_produto = pp.id_produto and
		pp.id_pedido = 1;

-- Questão 05: Listar a quantidade de pedidos realizados pelo cliente com nome = ‘Beltrano’. --
select  count(*)
from    clientes c, pedidos p
where   p.id_cliente = c.id_cliente and
         c.nome = 'Beltrano';
 
-- Questão 06: Calcular o valor total do pedido com id = 2 --
select	sum(pp.quantidade * pp.preco_unitario) as total_pedido
from 	pedidos_produtos pp
where 	pp.id_pedido = 2;

-- Questão 07: Calcular o valor total de todos os pedidos do cliente com id = 1. --
select	sum(pp.quantidade * pp.preco_unitario)
from	pedidos_produtos pp, pedidos p 	
where 	p.id_pedido = pp.id_pedido and
		p.id_cliente = 2;