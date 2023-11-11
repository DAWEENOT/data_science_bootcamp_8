.open restaurant.db
.mode column


-- Filter Only customer that has phone  --
SELECT *
FROM customers
WHERE phone NOT LIKE " " ;


-- The Best Seller Menu --

SELECT 
  menu_name,
  menu_price,
  COUNT (*) AS "number of order",
  SUM (menu_price) AS "total sales"
FROM invoices
JOIN menus
ON invoices.menu_id = menus.menu_id
GROUP BY menu_name
ORDER by "number of order" DESC
LIMIT 1;

-- The Best Seller drink --
SELECT
  drink_name,
  drink_price,
  COUNT (*) AS "number of oder",
  SUM(drink_price) AS "Total_sales"
FROM invoices
JOIN drinks
ON invoices.drink_id = drinks.drink_id
GROUP BY drink_name
ORDER BY "number of order" DESC
LIMIT 1;

-- The Best Seller location --
SELECT
  COUNT(*) AS "number of customer",
  SUM(menu_price) AS "total_food",
  SUM(drink_price) AS "total_drink",
  SUM(menu_price) + SUM(drink_price) AS "total cost",
  locations.location_id,
  locations.location_name
FROM invoices
JOIN locations
ON invoices.location_id = locations.location_id
JOIN drinks
ON invoices.drink_id = drinks.drink_id
JOIN menus
ON invoices.menu_id = menus.menu_id
GROUP BY locations.location_id, locations.location_name
ORDER BY "number of customer" DESC;

-- CREATE VIEW --
CREATE VIEW IF NOT EXISTS customers_view AS 
  WITH sub1 AS
    (SELECT
        invoice_id,
        customers.customer_id,
        firstname || " " || lastname AS customer_name,
        menu_price,
        drink_price,
        location_name,
        menu_price + drink_price AS total_price
      FROM invoices
      JOIN customers
        ON invoice.customer_id = customers.cutomer_id
      JOIN menus
        ON invoice.menu_id = menus.munu_id
      ORDER BY firstname)
  
    SELECT
      customer_id,
      customer_name,
      SUM(total_price) AS "Total cost"
    FROM sub1
    GROUP BY customer_name
    ORDER BY customer_id;


  
WITH sub1 AS (
    SELECT * 
    FROM customers
    WHERE email LIKE '%gmail.com'
), sub2 AS (
    SELECT 
      location_id,
      location_name,
      COALESCE(location_name, "No information") AS clean_location
    FROM locations
    WHERE location_id = 'CNX'
)

SELECT 
  sub1.firstname,
  sub2.location_name
FROM sub1
JOIN sub2
ON sub1.customer_id = sub2.location_id;
