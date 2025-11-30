CREATE TABLE dim_shipping (
    shipping_id SERIAL PRIMARY KEY,
    shipping_code VARCHAR(10) NOT NULL UNIQUE,
    shipping_name VARCHAR(50) NOT NULL,
    delivery_days INTEGER NOT NULL
);
