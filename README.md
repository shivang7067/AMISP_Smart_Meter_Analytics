
# AMISP Smart Meter Analytics

## Project Overview
AMISP Smart Meter Analytics is an end-to-end data analytics project based on smart meter operations. The project focuses on analyzing consumer installation status, work orders, HES communication status and energy consumption.

## Project Objectives
- Analyze smart meter installation progress.
- Monitor consumer and work order status.
- Track MDM and HES communication performance.
- Analyze monthly and circle-wise energy consumption.
- Build an interactive Power BI dashboard.

## Tools & Technologies
- MySQL 8.0.46
- Microsoft Power BI
- Python
- VS Code
- GitHub

## Database Details
Database Name: `amisp_analystic`

| Table | Records |
|---|---:|
| consumer | 1,004 |
| location_master | 98 |
| work_order | 1,500 |
| meter_reading | 30,000 |

## Power BI Dashboard
The dashboard includes:

1. Total Consumers
2. Completed Consumers
3. Total Work Orders
4. Total Meter Readings
5. MDM Communication Status
6. HES Communication Status
7. Work Orders by Circle & Status
8. Circle-wise Energy Consumption
9. Monthly Energy Consumption
10. Circle-wise Consumer Distribution

## Data Validation
All major record counts and status distributions were validated using SQL queries in MySQL Workbench.

## Project Structure
```text
AMISP_Smart_Meter_Analytics/
│
├── data/
├── python/
├── sql/
├── README.md
```

## Note
This project uses a synthetic dataset created for learning and portfolio demonstration purposes. It does not contain actual consumer or utility company data.

