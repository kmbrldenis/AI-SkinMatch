-- user information data and skincare preferences


-- ================
--user data
-- ================

CREATE TABLE user_data ( 
    id INTEGER PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hash_password TEXT NOT NULL,
    skin_type VARCHAR(50),
    sens_level VARCHAR(50),
    budget_range VARCHAR(50)
);

-- ================
--prodcuts
-- ================

CREATE TABLE products ( --products
    product_id INTEGER PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

-- ================
-- ingredients
-- ================

CREATE TABLE ingredients ( -- ingredients
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    comedogenic_grade INTEGER,
    irritation_grade INTEGER
);

-- ================
-- product_ingredients
-- ================

CREATE TABLE product_ingredients (
    product_id INTEGER,
    ingredient_id INTEGER,
    PRIMARY KEY (product_id, ingredient_id)
);