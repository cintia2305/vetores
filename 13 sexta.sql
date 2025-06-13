show databases;
create database sistema_academico;

use sistema_academico;

CREATE TABLE alunos(
codigo int,
endereco varchar(255), 
telefone varchar(20), 
data_ano date, 
disciplina varchar(100), 
professor varchar(100),
nota decimal
);

show tables;


INSERT INTO alunos(
codigo,
telefone,
endereco,
data_ano,
disciplina,
professor,
nota
) values
(
 1,
'Rua Brant Horta, 161',
'(31)93457-8990',
'1973-06-13',
'Banco de Dados',
'Lucio',
'9.0'
);

select * from alunos;
create database if not exists sistema_academico;
