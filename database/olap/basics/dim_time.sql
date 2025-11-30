CREATE TABLE dim_time (
    time_id SERIAL PRIMARY KEY,
    sale_date DATE NOT NULL,
    fiscal_year INTEGER NOT NULL,
    quarter VARCHAR(2) NOT NULL,  -- '1Q'(4-6月), '2Q'(7-9月), '3Q'(10-12月), '4Q'(1-3月)
    month VARCHAR(3) NOT NULL,    -- 'Jan', 'Feb', 'Mar', ...
    day_of_week VARCHAR(10) NOT NULL,
    UNIQUE(sale_date)
);
