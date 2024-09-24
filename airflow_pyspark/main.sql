CREATE TABLE IF NOT EXISTS sales (
  id SERIAL PRIMARY KEY,
  product_name VARCHAR(100),
  quantity INT,
  price DECIMAL(10, 2),
  sale_date DATE
);

INSERT INTO sales (product_name, quantity, price, sale_date)
VALUES
  ('Product A', 10, 20.5, '2023-09-01'),
  ('Product B', 5, 15.0, '2023-09-01'),
  ('Product C', 12, 30.75, '2023-09-02');
