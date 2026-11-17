
import random
import csv
from datetime import date, timedelta

# ==================================
# 1. PROJECT SETTINGS
# ==================================

project_name = "AMISP Smart Meter Analytics"
total_consumers = 1000
total_locations = 98

print("Project:", project_name)
print("Total Consumers:", total_consumers)
print("Total Locations:", total_locations)


# ==================================
# 2. SAMPLE CONSUMER DATA
# ==================================

consumer_names = [
    "Rahul Sharma",
    "Amit Verma",
    "Priya Patel",
    "Neha Singh",
    "Karan Jain",
    "Pooja Gupta",
    "Rohit Yadav",
    "Anjali Mishra",
    "Vikas Soni",
    "Sneha Tiwari"
]

insttallation_status = [
    "Completed",
    "Pending",
    "In Progress",
    "Rejected"
]

consumer_category = [
    "Domestic",
    "Commercial",
    "Industrial"
]


# ==================================
# 3. GENERATE CONSUMER RECORDS
# ==================================

consumers = []

for i in range(total_consumers):

    installation_date = (
        date(2025, 1, 1)
        + timedelta(days=random.randint(0, 364))
    )

    consumer = {
        "consumer_id": 1001 + i,
        "consumer_name": random.choice(consumer_names),
        "insttallation_status": random.choice(insttallation_status),
        "consumer_category": random.choice(consumer_category),
        "location_id": random.randint(1, total_locations),
        "meter_number": "SM" + str(100001 + i),
        "installation_date": installation_date
    }

    consumers.append(consumer)


# ==================================
# 4. DISPLAY GENERATED DATA
# ==================================

print("\nTotal Generated Consumers:", len(consumers))

print("\nFirst Consumer:")
print(consumers[0])

print("\nLast Consumer:")
print(consumers[-1])


# ==================================
# 5. EXPORT DATA TO CSV
# ==================================

file_path = "data/consumers.csv"

with open(file_path, mode="w", newline="", encoding="utf-8") as file:

    fieldnames = [
        "consumer_id",
        "consumer_name",
        "insttallation_status",
        "consumer_category",
        "location_id",
        "meter_number",
        "installation_date"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(consumers)


print("\nCSV file created successfully:", file_path)
print("Total records exported:", len(consumers))
