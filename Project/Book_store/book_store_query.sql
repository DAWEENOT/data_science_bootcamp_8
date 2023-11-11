-- Select column --

SELECT * FROM books;
SELECT * FROM customers;
SELECT * FROM employees;
SELECT * FROM invoices;
SELECT * FROM stores;
SELECT * FROM orders;


-- bring the first character --

SELECT
	customer_id id,
    customer_firstname || " " || customer_lastname as full_name,
    email
FROM customers
WHERE customer_firstname LIKE "J%";

SELECT
	customer_id AS id,
    customer_firstname || " " || customer_lastname AS full_name,
    country,
    email
FROM customers
WHERE country LIKE "%A";


-- Questions --

-- What is the best seller books --

SELECT
	books.book_id,
    books.title,
    books.price,
    orders.quantity,
    orders.quantity * books.price AS "Total_sales"
FROM books
JOIN orders
	ON orders.book_id = books.book_id
GROUP BY books.title
ORDER BY "Total_sales" DESC;

-- Which customers are the most spending on books and what is the title name and author? --

SELECT
	customers.customer_id,
    customers.customer_firstname || " " || customers.customer_lastname AS "full_name",
    books.book_id,
    books.title,
    books.author,
    orders.quantity,
    books.price * orders.quantity AS "Total sales"
FROM customers
JOIN orders
	ON orders.customer_id = customers.customer_id
JOIN books
	ON orders.book_id = books.book_id
GROUP BY title
ORDER BY "Total sales" DESC;

-- Which date is a higher quantity? --
SELECT
	invoices.invoice_id,
    books.title,
    books.author,
    orders.quantity,
    invoices.invoice_date
FROM invoices
JOIN orders
	ON orders.invoice_id = invoices.invoice_id
JOIN books
	ON orders.book_id = books.book_id
GROUP BY invoices.invoice_date
ORDER BY orders.quantity DESC;
    
-- Which brand location is the most total sales limit 5 --
SELECT
	stores.store_id,
    stores.store_name,
    stores.location,
    books.title,
    invoices.quantity,
    books.price * invoices.quantity AS " Total sales"
FROM stores
JOIN invoices
	on invoices.store_id =  stores.store_id
JOIN books
	ON invoices.book_id = books.book_id
GROUP BY 6
ORDER BY "Total sales" DESC
LIMIT 5;
