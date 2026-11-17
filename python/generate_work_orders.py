

import random
import csv
from datetime import date, timedelta

# Project settings
total_work_orders = 1500

# Sample data
work_types = [
    "New Installation",
    "Meter Replacement",
    "Inspection",
    "Maintenance"
]

work_order_statuses = [
    "Completed",
    "Pending",
    "In Progress",
    "Rejected"
]

teams = [
    "Team A",
    "Team B",
    "Team C",
    "Team D",
    "Team E"
]

remarks_data = {
    "Completed": "Work completed successfully",
    "Pending": "Work awaiting assignment",
    "In Progress": "Work currently in progress",
    "Rejected": "Work rejected after verification"
}

work_orders = []

# Generate records
for i in range(total_work_orders):

    work_order_date = (
        date(2025, 1, 1)
        + timedelta(days=random.randint(0, 364))
    )

    status = random.choice(work_order_statuses)

    completion_date =date(2000,1,1)

    if status == "Completed":
        completion_date = (
            work_order_date
            + timedelta(days=random.randint(1, 15))
        )

    work_order = {
        "work_order_id": 5001 + i,
        "consumer_id": random.randint(1001, 2000),
        "work_order_date": work_order_date,
        "work_type": random.choice(work_types),
        "work_order_status": status,
        "assigned_team": random.choice(teams),
        "completion_date": completion_date,
        "remarks": remarks_data[status]
    }

    work_orders.append(work_order)

# Export CSV
file_path = "data/work_orders.csv"

fieldnames = [
    "work_order_id",
    "consumer_id",
    "work_order_date",
    "work_type",
    "work_order_status",
    "assigned_team",
    "completion_date",
    "remarks"
]

with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(work_orders)

print("Project: AMISP Smart Meter Analytics")
print("Total Work Orders:", len(work_orders))
print("CSV created successfully:", file_path)
print("First Work Order:", work_orders[0])
