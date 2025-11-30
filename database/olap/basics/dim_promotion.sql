CREATE TABLE dim_promotion (
    promotion_id SERIAL PRIMARY KEY,
    promotion_code VARCHAR(20) NOT NULL UNIQUE,
    promotion_name VARCHAR(100) NOT NULL,
    discount_rate DECIMAL(5,2),
    start_date DATE,
    end_date DATE
);
