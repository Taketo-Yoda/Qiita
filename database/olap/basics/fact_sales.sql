CREATE TABLE fact_sales (
    sales_id BIGSERIAL PRIMARY KEY,
    time_id INTEGER NOT NULL REFERENCES dim_time(time_id),
    region_id INTEGER NOT NULL REFERENCES dim_region(region_id),
    product_id INTEGER NOT NULL REFERENCES dim_product(product_id),
    segment_id INTEGER NOT NULL REFERENCES dim_customer_segment(segment_id),
    channel_id INTEGER NOT NULL REFERENCES dim_sales_channel(channel_id),
    promotion_id INTEGER NOT NULL REFERENCES dim_promotion(promotion_id),
    shipping_id INTEGER NOT NULL REFERENCES dim_shipping(shipping_id),
    -- メジャー（集計対象の数値）
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    sales_amount DECIMAL(12,2) NOT NULL,
    cost_amount DECIMAL(12,2) NOT NULL,
    profit_amount DECIMAL(12,2) NOT NULL
);

-- パフォーマンス向上のためのインデックス例
CREATE INDEX idx_fact_sales_time ON fact_sales(time_id);
CREATE INDEX idx_fact_sales_region ON fact_sales(region_id);
CREATE INDEX idx_fact_sales_product ON fact_sales(product_id);
CREATE INDEX idx_fact_sales_segment ON fact_sales(segment_id);
CREATE INDEX idx_fact_sales_channel ON fact_sales(channel_id);
CREATE INDEX idx_fact_sales_promotion ON fact_sales(promotion_id);
CREATE INDEX idx_fact_sales_shipping ON fact_sales(shipping_id);

-- 複合インデックス例
-- 使用頻度の高い組み合わせなどがあれば適宜作成
CREATE INDEX idx_fact_sales_time_region ON fact_sales(time_id, region_id);
CREATE INDEX idx_fact_sales_time_product ON fact_sales(time_id, product_id);
