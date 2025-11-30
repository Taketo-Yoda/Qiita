CREATE TABLE dim_customer_segment (
    segment_id SERIAL PRIMARY KEY,
    segment_code VARCHAR(10) NOT NULL UNIQUE,
    segment_name VARCHAR(50) NOT NULL,
    description TEXT
);
