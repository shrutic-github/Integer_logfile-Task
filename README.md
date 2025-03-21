# Integer_logfile-Task
1. Log File Analysis
Identifying Patterns
The log file contains multiple sections of structured data enclosed within START and END markers.
Each table starts with a marker in the format:   MAL03377:<TABLE NAME> START
and ends with: MAL03377:<TABLE NAME> END
Column headers are present at the beginning of the extracted data for most tables, separated by ; or spaces.

Identified Tables
The following structured tables were identified:
ALARM STATUS
Start Marker: MAL03377:ALARM STATUS START
End Marker: MAL03377:ALARM STATUS END
Columns: Date_Time, Severity, Object, Problem

AVG PRB BRANCH RSSI
Start Marker: MAL03377:AVG PRB BRANCH RSSI START
End Marker: MAL03377:AVG PRB BRANCH RSSI END
Columns: Cell, SECTOR_X_Branch_Y, AVG_ULRSSI, PRBGroup1-10, ..., PRBGrp90-

AVG PER BRANCH RSSI
Start Marker: MAL03377:AVG PER BRANCH RSSI START
End Marker: MAL03377:AVG PER BRANCH RSSI END
Columns: CELL, SC, FRU, BOARD, PUSCH, PUCCH, A, B, C, D, DELTA

RFBRANCH STATUS
Start Marker: MAL03377:RFBRANCH STATUS START
End Marker: MAL03377:RFBRANCH STATUS END
Columns: MO, auPortRef, dlAttenuation, dlTrafficDelay, reservedBy, rfPortRef, tmaRef, ulAttenuation, ulTrafficDelay

BASIC DETAIL

Start Marker: MAL03377:BASIC DETAIL START
End Marker: MAL03377:BASIC DETAIL END
Columns: Proxy, Adm State, Op. State, MO

HARDWARE INVENTORY
Start Marker: MAL03377:HARDWARE INVENTORY START
End Marker: MAL03377:HARDWARE INVENTORY END
Contains information about hardware components and connectivity.

2. Data Extraction Process

Approach Used
Read the log file: Open the file and read all lines into memory.
Identify table sections: Extract data only between defined START and END markers.
Ignore empty tables: If no data is found between markers, that table is skipped.
Format extracted data: Convert extracted lines into structured table format.
Save to Excel: Store data in separate sheets for each table, ensuring proper formatting.

Extraction Logic in Python
Read the log file.
Loop through each line, detecting START and END markers.
Store the data within markers in a dictionary.
Convert data into pandas DataFrame and save as an Excel file with proper column formatting.
Use xlsxwriter to wrap text for better readability.
