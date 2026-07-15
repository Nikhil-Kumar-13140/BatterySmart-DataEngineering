-- =====================================================
-- Battery Smart EV Analytics Platform
-- Database Setup Documentation
-- Author: Nikhil Kumar
-- =====================================================

-- Create Database
CREATE DATABASE IF NOT EXISTS battery_smart_db;

-- Select Database
USE battery_smart_db;

-- Create Main Table
CREATE TABLE IF NOT EXISTS ev_data (

    vin VARCHAR(20),
    county VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(20),
    postal_code INT,
    model_year INT,
    make VARCHAR(50),
    model VARCHAR(100),
    electric_vehicle_type VARCHAR(100),
    cafv_eligibility VARCHAR(255),
    electric_range DOUBLE,
    base_msrp DOUBLE,
    dol_vehicle_id BIGINT,
    vehicle_location VARCHAR(255),
    electric_utility VARCHAR(255),
    census_tract BIGINT

);

-- Verify Structure
DESCRIBE ev_data;

-- Verify Data Import
SELECT COUNT(*) AS total_records
FROM ev_data;

-- Preview Imported Data
SELECT *
FROM ev_data
LIMIT 10;