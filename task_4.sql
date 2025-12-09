-- task_4.sql
-- Full description of the table books without using DESCRIBE or EXPLAIN

SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    DATA_TYPE, 
    CHARACTER_MAXIMUM_LENGTH, 
    IS_NULLABLE, 
    COLUMN_DEFAULT, 
    EXTRA 
FROM 
    INFORMATION_SCHEMA.COLUMNS 
WHERE 
    TABLE_SCHEMA = 'alx_book_store' 
    AND TABLE_NAME = 'Books'
ORDER BY 
    ORDINAL_POSITION;
