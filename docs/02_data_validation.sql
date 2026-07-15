-- =====================================================
-- Data Validation Queries
-- =====================================================

-- Total Records
SELECT COUNT(*) AS total_records
FROM ev_data;

-- Null Values Check
SELECT *
FROM ev_data
WHERE electric_range IS NULL;

-- Unique Manufacturers
SELECT COUNT(DISTINCT make) AS manufacturers
FROM ev_data;

-- Unique Models
SELECT COUNT(DISTINCT model) AS models
FROM ev_data;

-- Duplicate VIN Check
SELECT vin, COUNT(*)
FROM ev_data
GROUP BY vin
HAVING COUNT(*) > 1;

-- Preview Dataset
SELECT *
FROM ev_data
LIMIT 20;