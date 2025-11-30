CREATE TABLE dim_sales_channel (
    channel_id SERIAL PRIMARY KEY,
    channel_code VARCHAR(10) NOT NULL UNIQUE,
    channel_name VARCHAR(50) NOT NULL,
    channel_type VARCHAR(20) NOT NULL
);
