create table if not exists curso(
nome varchar(30) not null unique,
descrição text,
carga int unsigned,
totaulas int unsigned,
ano year default '2016'
)default charset utf8;

alter table curso
add column idcurso int first;

alter table curso
add primary key(idcurso);

insert into curso values
('1', 'HTML4', 'Curso de HTML5', '40','37', '2014'),
('2', 'Algoritmos', 'Logica de Programacao', '20', '15', '2014'),
('3', 'Photoshop', 'Dicas de Photoshop CC', '10', '8','2014'),
('4', 'PGP', 'Curso de PHP para iniciantes', '40', '20', '2010'),
('5', 'Jarva', 'Introducao a Linguagem Java', '10','29', '2000'),
('6', 'MySQL', 'Bancos de Dados MySQL','30','15','2016'),
('7', 'Word', 'Curso completo de Word','40', '30', '2016'),
('8', 'Sapateado', 'Dancas Rítmicas', '40', '30', '2018' ),
('9', 'Cozinha Arabe', 'Aprenda a fazer Kibe', '40','30','2018'),
('10', 'YouTuber', 'Gerar polemica e ganhar inscritos', '5', '2', '2018');

update curso
set nome = 'HTML5'
where idcurso = '1';

update curso
set nome = 'PHP', ano = '2015'
where idcurso = '4';

update curso
set nome = 'Java',carga = '40', ano = '2015'
where idcurso = '5'
limit 1;

delete from curso
where idcurso = '8';

delete from curso
where idcurso = '9';

delete from curso
where idcurso = '10';

select * from curso;

truncate curso