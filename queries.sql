######################################## CRIAR E POPULAR BANCO DE DADOS ################################

CREATE SCHEMA IF NOT EXISTS `online_restaurant_management` DEFAULT CHARACTER SET utf8mb4;

USE `online_restaurant_management`;

CREATE TABLE IF NOT EXISTS `online_restaurant_management`.`client` (
  `CPF` CHAR(11) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `birthdate` DATE NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` CHAR(6) NOT NULL,
  `gender` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`CPF`));

############ REQUISITO FUNCIONAL ########
# 1- Cadastro de cliente na base de dados
INSERT INTO online_restaurant_management.client (CPF, name, birthdate, email, password, gender) 
VALUES ('17735348746','Alexandre Maia', '2015-12-12', 'brancoalex@example.com' ,'@7MaI#', 'Masculino');

CREATE TABLE IF NOT EXISTS `online_restaurant_management`.`address` (
  `addressId` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(120) NOT NULL,
  `alias` VARCHAR(45) NULL,
  `clientId` CHAR(11) NOT NULL,
  PRIMARY KEY (`addressId`),
  INDEX `fk_address_client_idx` (`clientId` ASC) VISIBLE,
  CONSTRAINT `fk_address_client`
    FOREIGN KEY (`clientId`)
    REFERENCES `online_restaurant_management`.`client` (`CPF`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

############ REQUISITO FUNCIONAL ##########
# 2- Cadastro de endereços na base de dados.
INSERT INTO online_restaurant_management.address (address, alias, clientId) 
VALUES ('Rua Azevedo, 62','Casa', '17735348746');

CREATE TABLE IF NOT EXISTS `online_restaurant_management`.`meal` (
  `mealId` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `sellerPrice` FLOAT NOT NULL,
  `instructions` VARCHAR(120) NULL DEFAULT NULL,
  `area` VARCHAR(45) NULL DEFAULT NULL,
  `category` VARCHAR(45) NULL DEFAULT NULL,
  `imageURL` VARCHAR(120) NULL DEFAULT NULL,
  PRIMARY KEY (`mealId`));

############ REQUISITO FUNCIONAL ###########
#3 Cadastro de refeições e seus respectivos estoques na base de dados.
#3.1 Cadastro de refeições.
INSERT INTO `online_restaurant_management`.`meal` (mealId, name, sellerPrice, instructions, area, category, imageURL) 
VALUES (1,'Macarrão Bolonhesa', 49.90, 'Cozinha a carne, misture com molho de tomate, e coloque por cima do macarrão já cozido. Queijo parmesão à gosto','Itália','Massa', 'https:\/\/www.themealdb.com\/images\/media\/meals\/xr0n4r1576788363.jpg');

#3.2 Cadastro da refeição no estoque.
CREATE TABLE IF NOT EXISTS `online_restaurant_management`.`meal_stock` (
  `mealId` INT NOT NULL,
  `currentQuantity` INT NOT NULL,
  `idealQuantity` INT NOT NULL,
  `costPrice` FLOAT NOT NULL,
  PRIMARY KEY (`mealId`),
  CONSTRAINT `fk_mealId_stock`
    FOREIGN KEY (`mealId`)
    REFERENCES `online_restaurant_management`.`meal` (`mealId`));
    
INSERT INTO `online_restaurant_management`.`meal_stock` (mealId, currentQuantity, idealQuantity, costPrice) 
VALUES(1, 500, 50, 15.90);

######### REQUISITO FUNCIONAL ##############
#5 Criar pedido associado a um cliente, a um endereço e respectivas refeições.
CREATE TABLE IF NOT EXISTS `online_restaurant_management`.`order` (
  `orderId` INT NOT NULL AUTO_INCREMENT,
  `clientId` CHAR(11) NOT NULL,
  `addressId` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `totalPrice` FLOAT NOT NULL,
  `note` VARCHAR(120) NULL,
  PRIMARY KEY (`orderId`),
  INDEX `client_cpf_index` (`clientId` ASC) VISIBLE,
  INDEX `fk_addressId_orderId_idx` (`addressId` ASC) VISIBLE,
  CONSTRAINT `fk_clientId_orderId`
    FOREIGN KEY (`clientId`)
    REFERENCES `online_restaurant_management`.`client` (`CPF`),
  CONSTRAINT `fk_addressId_orderId`
    FOREIGN KEY (`addressId`)
    REFERENCES `online_restaurant_management`.`address` (`addressId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION) ;
    
INSERT INTO `online_restaurant_management`.`order` (clientId, addressId, date, totalPrice, note)
VALUES ('17735348746', 1, '2023-05-15', 49.90, 'Sem parmesão, por favor');

CREATE TABLE IF NOT EXISTS `online_restaurant_management`.`order_meal` (
  `orderId` INT NOT NULL,
  `mealId` INT NOT NULL,
  `quantity` INT NOT NULL DEFAULT '1',
  `totalPrice` FLOAT NOT NULL,
  CONSTRAINT `fk_mealId_orderId`
    FOREIGN KEY (`mealId`)
    REFERENCES `online_restaurant_management`.`meal` (`mealId`),
  CONSTRAINT `fk_orderId_mealId`
    FOREIGN KEY (`orderId`)
    REFERENCES `online_restaurant_management`.`order` (`orderId`));
    
INSERT INTO `online_restaurant_management`.`order_meal` (orderId, mealId, quantity, totalPrice)
VALUES (1, 1, 1, 49.90);

####### REQUISITO FUNCIONAL #####
#8 Criar ordem de estoque.
CREATE TABLE IF NOT EXISTS `online_restaurant_management`.`stock_order` (
  `stockOrderId` INT NOT NULL AUTO_INCREMENT,
  `mealId` INT NOT NULL,
  `totalPrice` FLOAT NOT NULL,
  `date` DATETIME NOT NULL,
  `quantity` INT NOT NULL,
  INDEX `mealId_index` (`mealId` ASC) VISIBLE,
  PRIMARY KEY (`stockOrderId`),
  CONSTRAINT `fk_mealId_stockOrderId`
    FOREIGN KEY (`mealId`)
    REFERENCES `online_restaurant_management`.`meal_stock` (`mealId`));
    
INSERT INTO `online_restaurant_management`.`stock_order` (mealId, totalPrice, date, quantity)
VALUES( 1, 7950, '2023-05-15 22:13:35', 500);

CREATE TABLE IF NOT EXISTS `online_restaurant_management`.`transaction` (
  `transactionId` INT NOT NULL AUTO_INCREMENT,
  `value` FLOAT NOT NULL,
  `date` DATETIME NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `orderId` INT,
  `stockOrderId` INT,
  PRIMARY KEY (`transactionId`),
  FOREIGN KEY (`orderId`)
	REFERENCES  `online_restaurant_management`.`order` (`orderId`),
  FOREIGN KEY (`stockOrderId`)
    REFERENCES  `online_restaurant_management`.`stock_order` (`stockOrderId`));

####### REQUISITO FUNCIONAL ########
#7 Criar transações financeiras de entradas e saídas do fluxo de caixa.    
INSERT INTO `online_restaurant_management`.`transaction` (value, date, name, orderId, stockOrderId)
VALUES 
(100000, '2023-05-15 22:00:35', 'Initial Amount', NULL, NULL),(-8000, '2023-05-15 15:00:35', 'Rental', NULL, NULL),
(-20000, '2023-05-15 22:01:35', 'Employees Salaries Amount', NULL, NULL),
(-5000, '2023-05-15 22:02:35', 'Maintanance', NULL, NULL),
(-7750, '2023-05-15 20:03:35', 'Meal Stock', NULL, 1),
(49.90, '2023-05-15 20:00:01', 'Order', 1, NULL);

######### REQUISITOS FUNCIONAIS ######################
#4 - Verificar disponibilidade de refeições no estoque.
SELECT mealId, 
       CASE WHEN currentQuantity >= 1 THEN TRUE ELSE FALSE END AS quantidade_disponivel
FROM meal_stock;

#6 - Atualizar quantidade de refeições em estoque
UPDATE meal_stock SET currentQuantity = currentQuantity - 1 WHERE mealId = 1;

#9 - Visualizar a soma de todas as receitas geradas por pedidos no período
SELECT * FROM transaction
WHERE value > 0
AND date BETWEEN '2023-05-01 00:00:00' AND '2023-05-31 00:00:00'
AND name LIKE '%Order%';

#10 Visualizar a quantidade de pedidos feitos no período.
SELECT COUNT(*) FROM `order` WHERE date BETWEEN '2023-05-01 00:00:00' AND '2023-05-31 00:00:00';

#11 Visualizar a quantidade total de clientes.
SELECT COUNT(*) FROM client;

#12 Visualizar a soma dos gastos por categoria: gastos com estoque, gastos gerais.
SELECT 
    SUM(CASE WHEN value < 0 AND name LIKE '%Salaries%' THEN value ELSE 0 END) as salary_expenses,
    SUM(CASE WHEN value < 0 AND name LIKE '%Maintanance%' THEN value ELSE 0 END) as maintenance_expenses,
    SUM(CASE WHEN value < 0 AND name LIKE '%Stock%' THEN value ELSE 0 END) as stock_expenses,
    SUM(CASE WHEN value < 0 AND name LIKE '%Rental%' THEN value ELSE 0 END) as rental_expenses
FROM transaction;

#13 Leitura de todos os clientes cadastrados na base de dados.
SELECT * FROM client;

#14 Visualizar refeições mais e menos pedidas por período.
SELECT om.mealId, m.name, SUM(om.quantity) as total_quantity
FROM `order_meal` as om 
INNER JOIN `meal` as m
	ON om.mealId = m.mealId
INNER JOIN `order` as o
	ON o.orderId = om.orderId
WHERE o.date BETWEEN '2023-05-01 00:00:00' AND '2023-05-31 00:00:00'
GROUP BY om.mealId, m.name
ORDER BY total_quantity DESC;

#14 Visualizar refeições mais e menos pedidas por período.
SELECT M.mealId, M.name, SUM(OM.quantity) as total_quantity 
FROM `order_meal` as OM
JOIN `meal` as M
	ON OM.mealId = M.mealId
GROUP BY M.mealId, M.name
ORDER BY total_quantity DESC;

#15 Visualizar os 10 clientes que mais compraram, em valor total por período. 
SELECT c.name, c.CPF, SUM(o.totalPrice) as value_purchases
FROM `client` as c
INNER JOIN `order` as o
	ON c.CPF = o.clientId
WHERE o.date BETWEEN '2023-05-01 00:00:00' AND '2023-05-31 00:00:00'
GROUP BY c.name, c.CPF
ORDER BY value_purchases DESC
LIMIT 10;
