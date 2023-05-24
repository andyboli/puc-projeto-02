from dotenv import dotenv_values


env = dotenv_values('.env')

CONNECTION_CONFIG = {
    'host': env['HOST'],
    'password': env['PASSWORD'],
    'raise_on_warnings': True,
    'user': env['USER'],
}

DB = 'online_restaurant_management'

DB_CREATE_QUERY = 'CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET "UTF8MB4"'.format(
    db_name=DB)

DB_DROP_QUERY = 'DROP DATABASE IF EXISTS {db_name}'.format(db_name=DB)

DB_CLIENT = 'Client'

DB_CLIENT_BIRTHDATE_COLUMN = 'birthdate'
DB_CLIENT_CPF_COLUMN = 'cpf'
DB_CLIENT_EMAIL_COLUMN = 'email'
DB_CLIENT_GENDER_COLUMN = 'gender'
DB_CLIENT_NAME_COLUMN = 'name'
DB_CLIENT_PASSWORD_COLUMN = 'password'

DB_CLIENT_COLUMNS = (DB_CLIENT_CPF_COLUMN,
                     DB_CLIENT_NAME_COLUMN,
                     DB_CLIENT_BIRTHDATE_COLUMN,
                     DB_CLIENT_EMAIL_COLUMN,
                     DB_CLIENT_PASSWORD_COLUMN, DB_CLIENT_GENDER_COLUMN)


DB_CLIENT_CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS {db_name}.{table_name}(
    {0} CHAR(11) NOT NULL,
    {1} VARCHAR(45) NOT NULL,
    {2} DATE NOT NULL,
    {3} VARCHAR(45) NOT NULL,
    {4} CHAR(6) NOT NULL,
    {5} VARCHAR(45) NULL DEFAULT NULL,
    PRIMARY KEY ({0}))
    ENGINE = InnoDB'''.format(db_name=DB, table_name=DB_CLIENT, *DB_CLIENT_COLUMNS)

DB_ADDRESS = 'Address'

DB_ADDRESS_ID_COLUMN = 'addressId'
DB_ADDRESS_CLIENT_ID_COLUMN = 'clientId'
DB_ADDRESS_ADDRESS_COLUMN = 'address'
DB_ADDRESS_ALIAS_COLUMN = 'alias'

DB_ADDRESS_COLUMNS = (DB_ADDRESS_ID_COLUMN,
                      DB_ADDRESS_CLIENT_ID_COLUMN, DB_ADDRESS_ADDRESS_COLUMN, DB_ADDRESS_ALIAS_COLUMN)

DB_ADDRESS_CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS {db_name}.{table_name}(
    {0} INT NOT NULL AUTO_INCREMENT,
    {1} CHAR(11) NOT NULL,
    {2} VARCHAR(120) NOT NULL,
    {3} VARCHAR(45) NULL,
    PRIMARY KEY (`addressId`),
    INDEX `fk_clientId_addressId_idx` ({1} ASC) VISIBLE,
    CONSTRAINT `fk_clientId_addressId`
        FOREIGN KEY ({1})
        REFERENCES {db_name}.{fk_table} ({fk_column})
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
    ENGINE = InnoDB'''.format(db_name=DB, table_name=DB_ADDRESS, fk_table=DB_CLIENT, fk_column=DB_CLIENT_CPF_COLUMN, *DB_ADDRESS_COLUMNS)


DB_MEAL = 'Meal'

DB_MEAL_ID_COLUMN = 'mealId'
DB_MEAL_NAME_COLUMN = 'name'
DB_MEAL_SELLER_PRICE_COLUMN = 'sellerPrice'
DB_MEAL_INSTRUCTIONS_COLUMN = 'instructions'
DB_MEAL_AREA_COLUMN = 'area'
DB_MEAL_CATEGORY_COLUMN = 'category'
DB_MEAL_IMAGE_URL_COLUMN = 'imageUrl'


DB_MEAL_COLUMNS = (DB_MEAL_ID_COLUMN, DB_MEAL_NAME_COLUMN, DB_MEAL_SELLER_PRICE_COLUMN, DB_MEAL_INSTRUCTIONS_COLUMN, DB_MEAL_AREA_COLUMN,
                   DB_MEAL_CATEGORY_COLUMN, DB_MEAL_IMAGE_URL_COLUMN)


DB_MEAL_CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS {db_name}.{table_name}(
    {0} INT NOT NULL,
    {1} VARCHAR(45) NOT NULL,
    {2} FLOAT NOT NULL,
    {3} VARCHAR(4000) NULL DEFAULT NULL,
    {4} VARCHAR(45) NULL DEFAULT NULL,
    {5} VARCHAR(45) NULL DEFAULT NULL,
    {6} VARCHAR(120) NULL DEFAULT NULL,
    PRIMARY KEY ({0}))
    ENGINE = InnoDB'''.format(db_name=DB, table_name=DB_MEAL, *DB_MEAL_COLUMNS)


DB_MEAL_INSERT_QUERY = 'INSERT INTO {db_name}.{table_name} (mealId, name, sellerPrice, instructions, area, category, imageUrl) '.format(
    db_name=DB, table_name=DB_MEAL) + '''VALUES (%s, %s, %s, %s, %s, %s, %s)'''

DB_MEAL_STOCK = 'MealStock'

DB_MEAL_STOCK_CURRENT_QNT_COLUMN = 'currentQuantity'
DB_MEAL_STOCK_LOWEST_QNT_COLUMN = 'lowestQuantity'
DB_MEAL_STOCK_COST_PRICE_COLUMN = 'costPrice'

DB_MEAL_STOCK_COLUMNS = (DB_MEAL_ID_COLUMN, DB_MEAL_STOCK_CURRENT_QNT_COLUMN,
                         DB_MEAL_STOCK_LOWEST_QNT_COLUMN, DB_MEAL_STOCK_COST_PRICE_COLUMN)

DB_MEAL_STOCK_CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS {db_name}.{table_name}(
    {0} INT NOT NULL,
    {1} INT NOT NULL,
    {2} INT NOT NULL,
    {3} FLOAT NOT NULL,
    PRIMARY KEY ({0}),
    CONSTRAINT `fk_mealId_stock`
        FOREIGN KEY ({0})
        REFERENCES {db_name}.{fk_table} ({0})
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
    ENGINE = InnoDB'''.format(db_name=DB, table_name=DB_MEAL_STOCK, fk_table=DB_MEAL, *DB_MEAL_STOCK_COLUMNS)

DB_MEAL_STOCK_INSERT_QUERY = 'INSERT INTO {db_name}.{table_name} (mealId, currentQuantity, lowestQuantity, costPrice) '.format(
    db_name=DB, table_name=DB_MEAL_STOCK) + '''VALUES (%s, %s, %s, %s)'''

DB_MEAL_STOCK_AFTER_UPDATE_TRIGGER = ''' CREATE DEFINER = CURRENT_USER TRIGGER `puc_database_restaurant`.`create_stock_order` AFTER UPDATE ON `meal_stock` FOR EACH ROW
BEGIN
	-- Verificação (SELECT) da quantidade de estoque (meal_stock).
	-- Se a currentQuantity for menor que a idealQuantity (meal_stock) criar (INSERT) uma stock_order.
END '''

DB_ORDER = 'Order'

DB_ORDER_ID_COLUMN = 'orderId'
DB_ORDER_CLIENT_ID_COLUMN = 'clientId'
DB_ORDER_ADDRESS_ID_COLUMN = 'addressId'
DB_ORDER_DATE_COLUMN = 'date'
DB_ORDER_TOTAL_PRICE_COLUMN = 'totalPrice'
DB_ORDER_NOTE_COLUMN = 'note'

DB_ORDER_COLUMNS = (DB_ORDER_ID_COLUMN,
                    DB_ORDER_CLIENT_ID_COLUMN, DB_ORDER_ADDRESS_ID_COLUMN, DB_ORDER_DATE_COLUMN, DB_ORDER_TOTAL_PRICE_COLUMN, DB_ORDER_NOTE_COLUMN)

DB_ORDER_CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS {db_name}.{table_name}(
    {0} INT NOT NULL AUTO_INCREMENT,
    {1} CHAR(11) NOT NULL,
    {2} INT NOT NULL,
    {3} DATETIME NOT NULL,
    {4} FLOAT NOT NULL,
    {5} VARCHAR(120) NULL,
    PRIMARY KEY ({0}),
    INDEX `client_cpf_index` ({1} ASC) VISIBLE,
    INDEX `fk_addressId_orderId_idx` ({2} ASC) VISIBLE,
    CONSTRAINT `fk_clientCpf_orderId`
        FOREIGN KEY ({1})
        REFERENCES {db_name}.{fk_table_1} ({fk_column_1}),
    CONSTRAINT `fk_addressId_orderId`
        FOREIGN KEY ({2})
        REFERENCES {db_name}.{fk_table_2} ({fk_column_2})
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
    ENGINE = InnoDB'''.format(db_name=DB, table_name=DB_ORDER,
                              fk_table_1=DB_CLIENT,
                              fk_column_1=DB_CLIENT_CPF_COLUMN,
                              fk_table_2=DB_ADDRESS,
                              fk_column_2=DB_ADDRESS_ID_COLUMN,
                              *DB_ORDER_COLUMNS)

DB_ORDER_BEFORE_INSERT_TRIGGER = '''CREATE DEFINER = CURRENT_USER TRIGGER {db_name}.`check_meal_availability` BEFORE INSERT ON {table_name} FOR EACH ROW
BEGIN
    SELECT {DB_MEAL_STOCK_CURRENT_QNT_COLUMN}, {DB_MEAL_STOCK_LOWEST_QNT_COLUMN} FROM {db_name}.{DB_MEAL_STOCK} WHERE {DB_MEAL_ID_COLUMN} = {mealId}
	IF ({DB_MEAL_STOCK_CURRENT_QNT_COLUMN} >= {DB_MEAL_STOCK_LOWEST_QNT_COLUMN})
		CONTINUE
    ELSE
		ROLLBACK

	-- Verificação da quantidade de refeições disponíveis.
    -- Se a quantidade pedida da refeição estiver disponível, encerra a transaction e continua e inserção.
    -- Se a quantidade pedida da refeição não estiver disponível, 
    -- If not currentQuantity >= quantity: ROLLBACK
END'''

DB_ORDER_AFTER_INSERT_TRIGGER = '''CREATE DEFINER = CURRENT_USER TRIGGER {db_name}.`create_order_meal_and_create_order_transaction` AFTER INSERT ON `order` FOR EACH ROW
BEGIN
	-- Criação (INSERT) de uma transação de entrada de dinheiro com a propriedade code sendo orderId (transaction). 
    -- Registro (INSERT) dos pratos inclusos no pedido (order_meal).
END'''


DB_ORDER_MEAL = 'OrderMeal'

DB_ORDER_MEAL_ID_COLUMN = 'orderMealId'
DB_ORDER_MEAL_QUANTITY_COLUMN = 'quantity'
DB_ORDER_TOTAL_PRICE_COLUMN = 'totalPrice'

DB_ORDER_MEAL_COLUMNS = (DB_ORDER_MEAL_ID_COLUMN,
                         DB_ORDER_ID_COLUMN, DB_MEAL_ID_COLUMN, DB_ORDER_MEAL_QUANTITY_COLUMN, DB_ORDER_TOTAL_PRICE_COLUMN)


DB_ORDER_MEAL_CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS {db_name}.{table_name}(
    {0} INT NOT NULL AUTO_INCREMENT,
    {1} INT NOT NULL,
    {2} INT NOT NULL,
    {3} INT NOT NULL DEFAULT '1',
    {4} FLOAT NOT NULL,
    INDEX `orderId_index` ({0} ASC) VISIBLE,
    INDEX `mealId_index` ({1} ASC) VISIBLE,
    PRIMARY KEY ({0}, {1}),
    CONSTRAINT `fk_orderId_mealId`
        FOREIGN KEY ({1})
        REFERENCES {db_name}.{fk_table_1} ({1})
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT `fk_mealId_orderId`
        FOREIGN KEY ({2})
        REFERENCES {db_name}.{fk_table_2} ({2})
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
    ENGINE = InnoDB'''.format(db_name=DB, table_name=DB_ORDER_MEAL, fk_table_1=DB_ORDER, fk_table_2=DB_MEAL, *DB_ORDER_MEAL_COLUMNS)


DB_ORDER_MEAL_AFTER_INSERT_TRIGGER = ''' CREATE DEFINER = CURRENT_USER TRIGGER `puc_database_restaurant`.`decress_meal_stock` AFTER INSERT ON `order_meal` FOR EACH ROW
BEGIN
 -- Diminuição (UPDATE) da quantidade de refeiçõs no estoque (meal_stock).
END '''

DB_STOCK_ORDER = 'StockOrder'

DB_STOCK_ORDER_ID_COLUMN = 'stockOrderId'
DB_STOCK_ORDER_TOTAL_PRICE_COLUMN = 'totalPrice'
DB_STOCK_ORDER_DATE_COLUMN = 'date'
DB_STOCK_ORDER_QUANTITY_COLUMN = 'quantity'

DB_STOCK_ORDER_COLUMNS = (DB_STOCK_ORDER_ID_COLUMN, DB_MEAL_ID_COLUMN,
                          DB_STOCK_ORDER_TOTAL_PRICE_COLUMN, DB_STOCK_ORDER_DATE_COLUMN, DB_STOCK_ORDER_QUANTITY_COLUMN)


DB_STOCK_ORDER_CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS {db_name}.{table_name}(
    {0} INT NOT NULL AUTO_INCREMENT,
    {1} INT NOT NULL,
    {2} FLOAT NOT NULL,
    {3} DATETIME NOT NULL,
    {4} INT NOT NULL,
    PRIMARY KEY ({0}),
    INDEX `mealId_index` ({1} ASC) VISIBLE,
    CONSTRAINT `fk_mealId_stockOrderId`
        FOREIGN KEY ({1})
        REFERENCES {db_name}.{fk_table} ({1})
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
    ENGINE = InnoDB'''.format(db_name=DB, table_name=DB_STOCK_ORDER, fk_table=DB_MEAL_STOCK, *DB_STOCK_ORDER_COLUMNS)

DB_STOCK_ORDER_AFTER_INSERT_TRIGGER = ''' CREATE DEFINER = CURRENT_USER TRIGGER `puc_database_restaurant`.`create_stock_order_transaction_and_update_meal_stock` AFTER INSERT ON `stock_order` FOR EACH ROW
BEGIN
	-- Criação (INSERT) de uma transação de saída de dinheiro com a propriedade code sendo orderId (transaction). 
    -- Aumenta (UPDATE) a quantidade de refeições (currentQuantity) no estoque (meal_stock).
END '''


DB_TRANSACTION = 'Transaction'

DB_TRANSACTION_ID_COLUMN = 'transactionId'
DB_TRANSACTION_VALUE_COLUMN = 'value'
DB_TRANSACTION_DATE_COLUMN = 'date'
DB_TRANSACTION_NAME_COLUMN = 'name'
DB_TRANSACTION_CODE_COLUMN = 'code'

DB_TRANSACTION_COLUMNS = (DB_TRANSACTION_ID_COLUMN,
                          DB_TRANSACTION_VALUE_COLUMN,
                          DB_TRANSACTION_DATE_COLUMN,
                          DB_TRANSACTION_NAME_COLUMN,
                          DB_TRANSACTION_CODE_COLUMN)


DB_TRANSACTION_CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS {db_name}.{table_name}(
    {0} INT NOT NULL AUTO_INCREMENT,
    {1} FLOAT NOT NULL,
    {2} DATETIME NOT NULL,
    {3} VARCHAR(45) NOT NULL,
    {4} INT NULL DEFAULT NULL,
    PRIMARY KEY ({0}),
    INDEX `code_idx` ({4} ASC) VISIBLE,
    CONSTRAINT `fk_stockOrderId_code`
        FOREIGN KEY ({4})
        REFERENCES {db_name}.{fk_table_1} ({fk_column_1}),
    CONSTRAINT `fk_orderId_code`
        FOREIGN KEY ({4})
        REFERENCES {db_name}.{fk_table_2} ({fk_column_2}))
    ENGINE = InnoDB'''.format(db_name=DB, table_name=DB_TRANSACTION, fk_table_1=DB_STOCK_ORDER, fk_column_1=DB_STOCK_ORDER_ID_COLUMN, fk_table_2=DB_ORDER, fk_column_2=DB_ORDER_ID_COLUMN, *DB_TRANSACTION_COLUMNS)


DB_TRANSACTION_INSERT_QUERY = 'INSERT INTO {db_name}.{table_name} (value, name, date, code) '.format(
    db_name=DB, table_name=DB_TRANSACTION) + '''VALUES (%s, %s, %s, %s)'''
