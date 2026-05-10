-- user information data and skincare preferences

CREATE TABLE user_data (
    id INTEGER PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hash_password TEXT NOT NULL,
    skin_type VARCHAR(50),
    sens_level VARCHAR(50),
    budget_range VARCHAR(50)
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    comedogenic_grade INTEGER,
    irritation_grade INTEGER
);

CREATE TABLE product_ingredients (
    product_id INTEGER,
    ingredient_id INTEGER
);