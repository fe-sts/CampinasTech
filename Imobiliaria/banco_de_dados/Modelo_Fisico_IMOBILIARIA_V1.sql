CREATE DATABASE imobiliarias
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8';

CREATE TABLE NOME_BANCO (
ID_BANCO SERIAL PRIMARY KEY,
NOME_BANCO VARCHAR(255)
);

CREATE TABLE VENDAS (
ID_VENDA SERIAL PRIMARY KEY,
ID_PROPRIETARIO SERIAL,
FOREIGN KEY (ID_PROPRIETARIO) REFERENCES PROPRIETARIOS (ID_PROPRIETARIO)
);

CREATE TABLE ENDERECOS (
ID_ENDERECO SERIAL PRIMARY KEY,
RUA VARCHAR(255),
NUMERO INTEGER,
COMPLEMENTO VARCHAR(100)
);

CREATE TABLE DESPESAS (
ID_DESPESA SERIAL PRIMARY KEY,
VLR_LUZ REAL,
VLR_CONDOMINIO REAL,
VLR_PROPAGANDA REAL
);

CREATE TABLE USUARIOS (
ID_USUARIO SERIAL PRIMARY KEY,
NOME_USUARIO VARCHAR(255)
);

CREATE TABLE CORRETORES (
ID_CORRETORES SERIAL PRIMARY KEY,
NOME_CORRETOR VARCHAR(255)
);

CREATE TABLE TELEFONES (
ID_TELEFONE SERIAL PRIMARY KEY,
TELEFONE INTEIRO
);

CREATE TABLE CLIENTES (
ID_CLIENTE SERIAL PRIMARY KEY,
NOME_CLIENTE VARCHAR(255),
CPF VARCHAR(100),
RG VARCHAR(100),
CEP VARCHAR(100),
DT_NASCIMENTO DATE,
ESTADO_CIVIL VARCHAR(100)
);

CREATE TABLE PROPRIETARIOS (
ID_PROPRIETARIO SERIAL PRIMARY KEY,
NOME_PROPRIETARIO VARCHAR(255),
CPF VARCHAR(100),
RG VARCHAR(100),
ESTADO_CIVIL VARCHAR(100),
TEMPO_IMO INTEGER,
PROFISSAO VARCHAR(255)
);

CREATE TABLE ITENS_VENDA (
ID_VENDA SERIAL,
ID_IMOVEL SERIAL,
ID_CLIENTE SERIAL,
VLR_VENDA REAL,
MODALIDADE VARCHAR(100),
FOREIGN KEY(ID_VENDA) REFERENCES VENDAS (ID_VENDA),
FOREIGN KEY(ID_CLIENTE) REFERENCES CLIENTES (ID_CLIENTE)
);

CREATE TABLE IMOVEIS (
ID_IMOVEL SERIAL PRIMARY KEY,
TIPO_IMOVEL VARCHAR(255),
IDADE_IMOVEL Inteiro,
LOGRADOURO VARCHAR(255),
NUMERO INTEGER,
BAIRRO Varchar(255),
ANDAR INTEGER,
BLOCO VARCHAR(100),
CEP VARCHAR(100),
CIDADE VARCHAR(255),
UF VARCHAR(255)
);

ALTER TABLE VENDAS ADD FOREIGN KEY(ID_PROPRIETARIO) REFERENCES PROPRIETARIOS (ID_PROPRIETARIO);
ALTER TABLE ITENS_VENDA ADD FOREIGN KEY(ID_IMOVEL) REFERENCES IMOVEIS (ID_IMOVEL);