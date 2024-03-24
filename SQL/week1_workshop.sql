-- Kill other connections to ensure smooth database recreation
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'week1_workshop' AND pid <> pg_backend_pid();

-- Drop and recreate the database
DROP DATABASE IF EXISTS week1_workshop;
CREATE DATABASE week1_workshop;

-- Connect to the newly created database
\c week1_workshop

-- Set database configuration options
SET statement_timeout = 0; -- Disable statement timeout
SET lock_timeout = 0; -- Disable lock timeout
SET client_encoding = 'UTF8'; -- Set client encoding to UTF-8
SET standard_conforming_strings = on; -- Enable standard conforming strings
SET check_function_bodies = false; -- Disable checking function bodies
SET client_min_messages = warning; -- Set minimum message level to warning
SET default_tablespace = ''; -- Set default tablespace
SET default_with_oids = false; -- Do not include OIDs by default

-- Create tables

-- Table for products
CREATE TABLE products (
    product_id SERIAL, -- Unique identifier for the product
    product_name TEXT NOT NULL, -- Name of the product
    discontinued INT NOT NULL, -- Indicates if the product is discontinued
    supplier_id INT, -- Foreign key referencing supplier table
    category_id INT, -- Foreign key referencing categories table
    PRIMARY KEY(product_id) -- Define product_id as the primary key
);

-- Table for product categories
CREATE TABLE categories (
    category_id SERIAL, -- Unique identifier for the category
    category_name TEXT NOT NULL, -- Name of the category
    category_description TEXT, -- Description of the category
    picture TEXT, -- Path to the picture representing the category
    PRIMARY KEY(category_id) -- Define category_id as the primary key
);

-- Table for suppliers
CREATE TABLE supplier (
    supplier_id SERIAL, -- Unique identifier for the supplier
    supplier_name TEXT NOT NULL, -- Name of the supplier
    PRIMARY KEY(supplier_id) -- Define supplier_id as the primary key
);

-- Table for orders
CREATE TABLE orders (
    order_id SERIAL, -- Unique identifier for the order
    order_date TIMESTAMP, -- Date and time when the order was placed
    PRIMARY KEY(order_id), -- Define order_id as the primary key
    customer_id INT, -- Foreign key referencing customer table
    employee_id INT, -- Foreign key referencing employee table
    shipper_id INT -- Foreign key referencing shipper table
);

-- Table for products in orders
CREATE TABLE product_orders (
    product_id INT NOT NULL, -- Foreign key referencing products table
    order_id INT NOT NULL, -- Foreign key referencing orders table
    PRIMARY KEY(product_id, order_id), -- Define composite primary key
    quantity INT NOT NULL, -- Quantity of the product in the order
    discount FLOAT NOT NULL -- Discount applied to the product in the order
);

-- Table for customers
CREATE TABLE customer (
    customer_id SERIAL, -- Unique identifier for the customer
    customer_companyname TEXT NOT NULL, -- Name of the customer's company
    PRIMARY KEY(customer_id) -- Define customer_id as the primary key
);

-- Table for shippers
CREATE TABLE shipper (
    shipper_id SERIAL, -- Unique identifier for the shipper
    shipper_name TEXT NOT NULL, -- Name of the shipper
    shipper_phone TEXT, -- Phone number of the shipper
    PRIMARY KEY(shipper_id) -- Define shipper_id as the primary key
);

-- Table for employees
CREATE TABLE employee (
    employee_id SERIAL, -- Unique identifier for the employee
    employee_firstname TEXT NOT NULL, -- First name of the employee
    employee_lastname TEXT NOT NULL, -- Last name of the employee
    PRIMARY KEY(employee_id), -- Define employee_id as the primary key
    manager_id INT -- Foreign key referencing manager employee
);

-- Table for employee territories
CREATE TABLE employee_territory (
    employee_id INT NOT NULL, -- Foreign key referencing employee table
    territory_id INT NOT NULL, -- Foreign key referencing territory table
    PRIMARY KEY(employee_id, territory_id) -- Define composite primary key
);

-- Table for territories
CREATE TABLE territory (
    territory_id SERIAL, -- Unique identifier for the territory
    territory_description TEXT NOT NULL, -- Description of the territory
    PRIMARY KEY(territory_id), -- Define territory_id as the primary key
    region_id INT NOT NULL -- Foreign key referencing region table
);

-- Table for regions
CREATE TABLE region (
    region_id SERIAL, -- Unique identifier for the region
    region_description TEXT NOT NULL, -- Description of the region
    PRIMARY KEY(region_id) -- Define region_id as the primary key
);

-- Table for US states
CREATE TABLE us_state (
    us_state_id SERIAL, -- Unique identifier for the US state
    us_state_name TEXT, -- Name of the US state
    us_state_abbreviation CHAR(2) NOT NULL, -- Abbreviation of the US state
    PRIMARY KEY(us_state_id) -- Define us_state_id as the primary key
);

-- Add foreign key constraints

-- Constraint for products referencing categories
ALTER TABLE products
ADD CONSTRAINT fk_products_categories 
FOREIGN KEY (category_id) 
REFERENCES categories;

-- Constraint for products referencing suppliers
ALTER TABLE products
ADD CONSTRAINT fk_products_suppliers
FOREIGN KEY (supplier_id)
REFERENCES supplier;

-- Constraint for product orders referencing products
ALTER TABLE product_orders
ADD CONSTRAINT fk_products_orders_products
FOREIGN KEY (product_id)
REFERENCES products;

-- Constraint for product orders referencing orders
ALTER TABLE product_orders
ADD CONSTRAINT fk_products_orders_orders
FOREIGN KEY (order_id)
REFERENCES orders;

-- Constraint for orders referencing customers
ALTER TABLE orders
ADD CONSTRAINT fk_order_customer
FOREIGN KEY (customer_id)
REFERENCES customer;

-- Constraint for orders referencing shippers
ALTER TABLE orders
ADD CONSTRAINT fk_order_shipper
FOREIGN KEY (shipper_id)
REFERENCES shipper;

-- Constraint for orders referencing employees
ALTER TABLE orders
ADD CONSTRAINT fk_order_employee
FOREIGN KEY (employee_id)
REFERENCES employee;

-- Constraint for territories referencing regions
ALTER TABLE territory
ADD CONSTRAINT fk_territory_region
FOREIGN KEY (region_id)
REFERENCES region;

-- Constraint for employee territories referencing employees
ALTER TABLE employee_territory
ADD CONSTRAINT fk_employee_territory_employee
FOREIGN KEY (employee_id)
REFERENCES employee;

-- Constraint for employee territories referencing territories
ALTER TABLE employee_territory
ADD CONSTRAINT fk_employee_territory_territory
FOREIGN KEY (territory_id)
REFERENCES territory;

-- Constraint for employees referencing manager employees
ALTER TABLE employee
ADD CONSTRAINT fk_employees_manager
FOREIGN KEY (manager_id)
REFERENCES employee;
