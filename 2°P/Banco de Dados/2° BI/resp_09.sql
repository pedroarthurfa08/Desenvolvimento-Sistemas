-- Questao 01: Selecionar a quantidade de emprestimos feitos pelo aluno com id = 2 --
select 	count(*)
from 	emprestimo e
where 	e.id_aluno =2;

-- Questao 02: Selecionar os titulos dos livros que já foram emprestados ao aluno com id = 2 --
select 	l.titulo
from 	livro l, emprestimo e
where	e.id_aluno = 2 and
		l.id = e.id_livro;
		
-- Questao 03: Listar o nome do aluno e o titulo do livro para cada emprestimo realizado --
select 	a.nome, l.titulo
from	aluno a, livro l, emprestimo e
where	a.id = e.id_aluno and
		l.id = e.id_livro;

-- Questao 04: Listar o nome do autor e o titulo de todos os livros que ele escreveu --
select 	a.nome, l.titulo
from	autor a, livro_autor la, livro l
where 	l.id = la.id_livro and
		la.id_autor = a.id;
        
-- Questao 05: Listar a quantidade de emprestimos de livros escritos pelo Machado de Assis --
select 	count(e.id)
from	emprestimo e, livro l, livro_autor la, autor a
where	a.nome = 'Machado de Assis' and
		la.id_autor = a.id and
        la.id_livro = l.id and
        l.id = e.id_livro;
