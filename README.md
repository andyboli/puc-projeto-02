# puc-projeto-02

## Etapas do projeto

Projeto Conceitual do Banco de Dados
Projeto Lógico do Banco de Dados
Projeto Físico do Banco de Dados
Dataframes em Python

### Etapa 1: Definição do grupo de trabalho e do objeto do projeto

Nesta etapa, você definirá a composição do grupo que conduzirá o projeto com você. Após a formação do grupo, vocês deverão definir o objeto do projeto, ou seja, o problema de negócio que irá se beneficiar do desenvolvimento do projeto de banco de dados.

### Etapa 2: Projeto Conceitual do Banco de Dados

Nesta etapa, seu grupo deverá descrever o minimundo, que é o universo de discurso da situação atual ou, ainda, a descrição do negócio a partir da perspectiva dos seus dados. Depois disso, esta descrição será representada em um modelo de dados, chamado de Diagrama Entidade Relacionamento (DER). Além disso, os requisitos funcionais com as consultas que serão submetidas ao banco de dados devem ser especificados.

### Etapa 3: Projeto Lógico do Banco de Dados

Nesta etapa, seu grupo irá traduzir o modelo de dados conceitual em um modelo lógico, baseado na classe de bancos de dados relacionais.

### Etapa 4: Projeto Físico do Banco de Dados

Nesta etapa, seu grupo deverá implementar o modelo lógico relacional em um SGBD, que deverá ser escolhido, definida a sua localização na rede, bem como ter as tabelas do banco de dados criadas e populadas e ter observado os seus aspectos de otimização.

### Etapa 5: Dataframes em Python

Nesta etapa, seu grupo deverá converter as tabelas e as consultas em dataframes e códigos Python, gerando um notebook em Python.

## Configuring and Running the Project

### Creating and Running the Virtual Enviroment

```sh
py -m venv .venv
.\.venv\Scripts\activate
```

### Installing Python Modules

```sh
py -m pip install -r requirements.txt
```

### Running the project

```sh
python -m index
```

## Installing Mysql

MySQL, the most popular Open Source SQL database management system, is developed, distributed, and supported by Oracle Corporation;
MySQL is a database management system. A database is a structured collection of data;
To add, access, and process data stored in a computer database, you need a database management system such as MySQL Server;
MySQL databases are relational;
A relational database stores data in separate tables rather than putting all the data in one big storeroom;
The SQL part of “MySQL” stands for “Structured Query Language”. SQL is the most common standardized language used to access databases;
MySQL software is Open Source. Open Source means that it is possible for anyone to use and modify the software;
The MySQL Database Server is very fast, reliable, scalable, and easy to use;
The MySQL Community Server provides a database management system with querying and connectivity capabilities, as well as the ability to have excellent data structure and integration with many different platforms;
The MySQL APT repository provides a simple and convenient way to install and update MySQL products with the latest software packages using Apt;
MySQL Workbench delivers visual tools for creating, executing, and optimizing SQL queries;

[MySQL Community Downloads](https://dev.mysql.com/downloads/)

MySQL Community Server[https://dev.mysql.com/downloads/mysql/]

MySQL Shell [https://dev.mysql.com/downloads/shell/]

MySQL Workbench[https://dev.mysql.com/downloads/workbench/]

Check if MySQL Shell Service Is Running:

```sh
mysqlsh --version
```

Log in to MySQL Server:

```sh
mysqlsh

\connect root@localhost:3306
```
