-- =====================================================
-- Business Analytics Queries
-- =====================================================

-- Total Vehicles
SELECT COUNT(*) AS total_vehicles
FROM ev_data;

-- Top 10 Manufacturers
SELECT
    make,
    COUNT(*) AS total_vehicles
FROM ev_data
GROUP BY make
ORDER BY total_vehicles DESC
LIMIT 10;

-- Average Electric Range
SELECT
    ROUND(AVG(electric_range),2) AS average_range
FROM ev_data;

-- Average MSRP
SELECT
    ROUND(AVG(base_msrp),2) AS average_msrp
FROM ev_data;

-- Vehicles by State
SELECT
    state,
    COUNT(*) AS vehicles
FROM ev_data
GROUP BY state
ORDER BY vehicles DESC;

-- Vehicle Type Distribution
SELECT
    electric_vehicle_type,
    COUNT(*) AS total
FROM ev_data
GROUP BY electric_vehicle_type;

-- CAFV Eligibility Distribution
SELECT
    cafv_eligibility,
    COUNT(*) AS total
FROM ev_data
GROUP BY cafv_eligibility;