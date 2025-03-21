import re
import pandas as pd

# Define the log file path
log_file_path = "HC_Log_2025-02-24_21-19-14.txt"

# Define table markers
table_markers = {
    "ALARM STATUS": ("ALARM STATUS START", "ALARM STATUS END"),
    "AVG PRB BRANCH RSSI": ("AVG PRB BRANCH RSSI START", "AVG PRB BRANCH RSSI END"),
    "AVG PER BRANCH RSSI": ("AVG PER BRANCH RSSI START", "AVG PER BRANCH RSSI END"),
    "RFBRANCH STATUS": ("RFBRANCH STATUS START", "RFBRANCH STATUS END"),
    "BASIC DETAIL": ("BASIC DETAIL START", "BASIC DETAIL END"),
    "HARDWARE INVENTORY": ("HARDWARE INVENTORY START", "HARDWARE INVENTORY END"),
}

# Read the log file
with open(log_file_path, "r", encoding="utf-8") as file:
    log_data = file.readlines()

# Function to extract table data
def extract_table(log_data, start_marker, end_marker):
    extracting = False
    table_data = []
    for line in log_data:
        if start_marker in line:
            extracting = True
            continue
        if end_marker in line:
            extracting = False
            break
        if extracting:
            table_data.append(line.strip())
    return table_data

# Extract tables
tables = {}
for table_name, markers in table_markers.items():
    tables[table_name] = extract_table(log_data, markers[0], markers[1])

# Function to save tables to Excel
def save_to_excel(tables, output_path):
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    for table_name, data in tables.items():
        df = pd.DataFrame([row.split(';') for row in data if row])
        df.to_excel(writer, sheet_name=table_name[:31], index=False, header=False)
    writer.close()

# Save extracted data
output_excel_path = "Extracted_table_data.xlsx"
save_to_excel(tables, output_excel_path)

print(f"Extracted data saved to {output_excel_path}")
