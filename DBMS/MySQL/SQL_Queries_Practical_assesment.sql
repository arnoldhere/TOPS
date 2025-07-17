create database tops_asess;
use tops_asess; 
CREATE TABLE country (
    country_id INT PRIMARY KEY,
    country VARCHAR(50)
);
CREATE TABLE city (
    city_id INT PRIMARY KEY,
    city VARCHAR(50),
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES country(country_id)
);
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES city(city_id)
);


INSERT INTO country (country_id, country) VALUES
(1, 'Germany'),
(2, 'Croatia'),
(3, 'USA'),
(4, 'Spain'),
(5, 'Russia');

-- Insert Data into city

INSERT INTO city (city_id, city, country_id) VALUES
(1, 'Berlin', 1),
(2, 'Zagreb', 2),
(3, 'New York', 3);

-- Insert Data into customer

INSERT INTO customer (customer_id, customer_name, city_id) VALUES
(1, 'Tom', 1),
(2, 'Ana', 2),
(3, 'John', 3),
(4, 'Mike', 1),
(5, 'Sara', 3);


-- All assesment practicals are below 
/*
1. List all countries and related customers 
*/
SELECT 
    co.country,
    ci.city,
    cu.customer_name
FROM 
    country co
LEFT JOIN city ci ON co.country_id = ci.country_id
LEFT JOIN customer cu ON ci.city_id = cu.city_id;

/*
2. Countries with cities (pairs), show customers (even if no customer)
*/
SELECT 
    co.country,
    ci.city,
    cu.customer_name
FROM 
    country co
INNER JOIN city ci ON co.country_id = ci.country_id
LEFT JOIN customer cu ON ci.city_id = cu.city_id;
