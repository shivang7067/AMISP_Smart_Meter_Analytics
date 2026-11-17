

import random
import csv
from datetime import date, timedelta

# ==================================
# 1. PROJECT SETTINGS
# ==================================

project_name = "AMISP Smart Meter Analytics"
total_readings = 30000
total_consumers = 1000

print("Project:", project_name)
print("Total Meter Readings:", total_readings)


# ==================================
# 2. SAMPLE DATA
# ==================================

mdm_statuses = [
    "Connected",
    "Disconnected",
    "Pending"
]

hes_statuses = [
    "Connected",
    "Disconnected",
    "Not Available"
]


# ==================================
# 3. GENERATE METER READINGS
# ==================================

meter_readings = []

for i in range(total_readings):

    consumer_id = random.randint(1001, 2000)

    meter_number = "SM" + str(consumer_id - 900)

    reading_date = (
        date(2025, 1, 1)
        + timedelta(days=random.randint(0, 364))
    )

    reading = {
        "reading_id": 100001 + i,
        "consumer_id": consumer_id,
        "meter_number": meter_number,
        "reading_date": reading_date,
        "kwh_consumption": round(random.uniform(5, 30), 2),
        "voltage": round(random.uniform(210, 250), 2),
        "current": round(random.uniform(1, 15), 2),
        "mdm_status": random.choice(mdm_statuses),
        "hes_status": random.choice(hes_statuses)
    }

    meter_readings.append(reading)


# ==================================
# 4. EXPORT TO CSV
# ==================================

file_path = "data/meter_readings.csv"

fieldnames = [
    "reading_id",
    "consumer_id",
    "meter_number",
    "reading_date",
    "kwh_consumption",
    "voltage",
    "current",
    "mdm_status",
    "hes_status"
]

with open(file_path, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(meter_readings)


# ==================================
# 5. FINAL OUTPUT
# ==================================

print("\nTotal Generated Readings:", len(meter_readings))
print("CSV Created Successfully:", file_path)
print("First Reading:", meter_readings[0])
