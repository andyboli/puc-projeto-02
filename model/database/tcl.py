def order_before_insert_trigger():
    

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

"""
try:

    db = mysql.connector.connect(option_files='my.conf', autocommit=True)

    cursor = db.cursor()

    db.start_transaction()

    # these two INSERT statements are executed as a single unit

    sql1 = 
    insert into employees(name, salary) value('Tom', 19000)


    sql2 =
    insert into employees(name, salary) value('Leo', 21000)
 

    cursor.execute(sql1)
    cursor.execute(sql2)

    db.commit()  # commit changes

    print('Transaction committed.')

except errors.Error as e:
    db.rollback()  # rollback changes
    print("Rolling back ...")
    print(e)

finally:
    cursor.close()
    db.close()


"""
