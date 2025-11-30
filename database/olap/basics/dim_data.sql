-- 1. 時間ディメンションのサンプルデータ
INSERT INTO dim_time (sale_date, fiscal_year, quarter, month, day_of_week) VALUES
('2025-01-15', 2024, '4Q', 'Jan', 'Monday'),
('2025-02-20', 2024, '4Q', 'Feb', 'Tuesday'),
('2025-03-10', 2024, '4Q', 'Mar', 'Sunday'),
('2025-04-05', 2025, '1Q', 'Apr', 'Friday'),
('2025-05-18', 2025, '1Q', 'May', 'Saturday'),
('2025-06-25', 2025, '1Q', 'Jun', 'Tuesday'),
('2025-07-12', 2025, '2Q', 'Jul', 'Friday'),
('2025-08-30', 2025, '2Q', 'Aug', 'Friday'),
('2025-09-14', 2025, '2Q', 'Sep', 'Saturday'),
('2025-10-22', 2025, '3Q', 'Oct', 'Tuesday'),
('2025-11-05', 2025, '3Q', 'Nov', 'Tuesday'),
('2025-11-18', 2025, '3Q', 'Nov', 'Monday'),
('2025-12-03', 2025, '3Q', 'Dec', 'Tuesday'),
('2025-12-20', 2025, '3Q', 'Dec', 'Friday');

-- 2. 地域ディメンションのサンプルデータ
INSERT INTO dim_region (region_code, region_name, prefecture) VALUES
('KANTO', '関東', '東京都'),
('KANSAI', '関西', '大阪府'),
('CHUBU', '中部', '愛知県'),
('KYUSHU', '九州', '福岡県'),
('TOHOKU', '東北', '宮城県');

-- 3. 商品ディメンションのサンプルデータ
INSERT INTO dim_product (product_code, product_name, category, subcategory) VALUES
('ELEC-001', 'ノートPC Type-X', '電化製品', 'パソコン'),
('ELEC-002', 'タブレット Pro', '電化製品', 'タブレット'),
('ELEC-003', 'スマートフォン Z', '電化製品', 'スマートフォン'),
('HOME-001', '冷蔵庫 500L', '家電', '冷蔵庫'),
('HOME-002', '洗濯機 10kg', '家電', '洗濯機'),
('FURN-001', 'オフィスチェア DX', '家具', '椅子'),
('FURN-002', 'デスク 120cm', '家具', 'デスク'),
('BOOK-001', 'ビジネス書籍A', '書籍', 'ビジネス'),
('BOOK-002', '技術書B', '書籍', '技術');

-- 4. 顧客セグメントディメンションのサンプルデータ
INSERT INTO dim_customer_segment (segment_code, segment_name, description) VALUES
('B2B', '法人顧客', '企業向け販売'),
('B2C-PRM', 'プレミアム個人', '高額商品を購入する個人顧客'),
('B2C-STD', '一般個人', '通常の個人顧客'),
('B2C-STU', '学生', '学生割引対象の顧客');

-- 5. 販売チャネルディメンションのサンプルデータ
INSERT INTO dim_sales_channel (channel_code, channel_name, channel_type) VALUES
('EC', 'ECサイト', 'オンライン'),
('STORE', '直営店舗', 'オフライン'),
('AGENCY', '代理店', 'オフライン'),
('MOBILE', 'モバイルアプリ', 'オンライン'),
('PHONE', '電話注文', 'オンライン');

-- 6. プロモーションディメンションのサンプルデータ
INSERT INTO dim_promotion (promotion_code, promotion_name, discount_rate, start_date, end_date) VALUES
('NONE', 'プロモーションなし', 0.00, NULL, NULL),
('SPRING25', '春の新生活キャンペーン', 15.00, '2025-03-01', '2025-04-30'),
('SUMMER25', '夏のボーナスセール', 20.00, '2025-06-15', '2025-07-31'),
('AUTUMN25', '秋の感謝祭', 10.00, '2025-09-01', '2025-09-30'),
('WINTER25', '年末大売出し', 25.00, '2025-11-20', '2025-12-31'),
('FLASH', 'フラッシュセール', 30.00, '2025-11-01', '2025-11-07');

-- 7. 配送方法ディメンションのサンプルデータ
INSERT INTO dim_shipping (shipping_code, shipping_name, delivery_days) VALUES
('STD', '通常配送', 3),
('EXPRESS', '速達配送', 1),
('ECO', 'エコ配送', 5),
('PICKUP', '店頭受取', 0);
