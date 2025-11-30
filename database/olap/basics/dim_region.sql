CREATE TABLE dim_region (
    region_id SERIAL PRIMARY KEY,
    region_code VARCHAR(10) NOT NULL UNIQUE,
    region_name VARCHAR(50) NOT NULL,
    prefecture VARCHAR(50)
);
